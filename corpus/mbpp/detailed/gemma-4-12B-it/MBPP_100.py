import math

def next_smallest_palindrome(n: int) -> int:
    """
    Finds the smallest palindrome strictly greater than the given integer n.

    Args:
        n (int): The starting integer.

    Returns:
        int: The next smallest palindrome.

    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    # Validation: Ensure the input is an integer.
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Validation: Negative numbers do not have a "next" palindrome in a standard sense
    # based on the problem context, but we handle them by converting to positive 
    # or rejecting. Here, we treat negative as invalid for this specific logic.
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # The problem asks for the next smallest palindrome (greater than n).
    # We start our search from n + 1.
    target = n + 1

    # Special case for single digits:
    # If n = 0, next is 1. If n = 8, next is 9.
    # If n = 9, next is 11.
    if target < 10:
        return target

    def is_palindrome(num: int) -> bool:
        """Helper to check if a number reads the same forwards and backwards."""
        s = str(num)
        return s == s[::-1]

    # Optimization: We don't want to increment by 1 indefinitely.
    # For large numbers, we can construct the palindrome based on the first half.

    current = target

    # Strategy:
    # 1. Try to mirror the first half of the current number.
    # 2. If that result is <= n, increment the middle and mirror again.

    s_str = str(current)
    length = len(s_str)

    # Case: All 9s (e.g., 99 -> 101, 999 -> 1001)
    # These result in a number with length + 1 digits.
    if all(char == '9' for char in s_str):
        # The next palindrome after 99...9 is 100...001
        # Example: 99 (length 2) -> 101
        # Example: 999 (length 3) -> 1001
        return 10**length + 1

    # Standard construction:
    # Get the first half of the number.
    # For 120 (len 3), first half is "12" (indices 0, 1) -> we only need "12"
    # For 1221 (len 4), first half is "12" (indices 0, 1)
    half_len = (length + 1) // 2
    first_half_str = s_str[:half_len]
    first_half_int = int(first_half_str)

    def construct_palindrome(prefix_int: int, total_len: int) -> int:
        """
        Constructs a palindrome from a prefix integer given the target total length.
        Example: prefix 12, total_len 3 -> 121
        Example: prefix 12, total_len 4 -> 1221
        """
        s_prefix = str(prefix_int)
        if total_len % 2 == 0:
            # Even length: prefix is "12", result is "12" + "21"
            suffix = s_prefix[::-1]
            return int(s_prefix + suffix)
        else:
            # Odd length: prefix is "12", result is "12" + "1"
            suffix = s_prefix[:-1][::-1]
            return int(s_prefix + suffix)

    # Candidate 1: Mirror the first half
    candidate1 = construct_palindrome(first_half_int, length)

    if candidate1 > n:
        return candidate1
    else:
        # Candidate 1 was smaller or equal to n.
        # We must increment the first half and mirror again.
        # This handles cases like 120 -> 121 (candidate 1 is 121 > 120)
        # and cases like 129 -> first_half 12 -> candidate 121 (which is < 129).
        # If candidate1 < target, we increment the prefix.
        new_prefix = first_half_int + 1

        # Check if incrementing the prefix increases the digit count.
        # e.g., 99 -> first_half 9 -> new_prefix 10.
        # If the length changes, the construct_palindrome logic needs to respect new length.
        new_prefix_str = str(new_prefix)

        # If the prefix length increased (e.g., 9 -> 10), the total length of the 
        # palindrome will increase by 1 or 2.
        # However, the "all 9s" check at the start handles the most common growth.
        # For cases like 199, first_half 19 -> 20 -> 202.

        # Re-calculate length based on new prefix.
        # If the prefix length is the same, the total length remains the same.
        # If the prefix length increased, we need to determine the new total length.
        if len(new_prefix_str) > len(first_half_str):
            # This part is hit if first_half was like 9, now 10.
            # The "all 9s" check usually catches these, but this is a safety net.
            # For example, n=999, first_half=99, new_prefix=100.
            # New length would be (len(new_prefix_str) * 2) - (1 if odd else 0)
            # But for simplicity, since 99...9 is caught, we just calculate:
            new_total_len = length + 1
            # If prefix was 9 (len 1) and became 10 (len 2), 
            # original length was 1 or 2. 
            # New length will be 3 if original was 2.
            # This logic is getting complex, so we fall back to a simple increment.
            # But we can just use the construct_palindrome with the new length.
            # A safer way to handle length increase is to just find the next length.
            # Let's simplify:
            new_total_len = len(new_prefix_str) * 2
            if (length % 2 != 0) and (len(new_prefix_str) == len(first_half_str)):
                new_total_len = len(new_prefix_str) * 2 - 1

            # To stay robust, let's use a simpler fallback for length changes:
            # If prefix length changes, the next palindrome is 10...01
            # which is handled by the 'all 9s' check or the next power of 10.
            # Let's just construct based on the new_prefix and a recalculated length.
            # If prefix was "9" (1) and became "10" (2), and total_len was 2 (even)
            # the new total_len is 3. If total_len was 1 (odd), new total_len is 2.
            # This is actually naturally handled by just trying to construct.

            # Since we already handled all 9s, the only way prefix length increases
            # is if we have something like 99... but that's caught.
            # Let's just use a standard construction.
            pass 

        # Because all 9s is caught, new_prefix_str length will be same as first_half_str.
        return construct_palindrome(new_prefix, length)