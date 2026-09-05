def is_palindrome(number: int) -> bool:
    """
    Check if a given integer is a palindrome.

    A palindrome number reads the same forwards and backwards.
    Negative numbers are never palindromes.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    # Negative numbers cannot be palindromes due to the minus sign
    if number < 0:
        return False

    # Single digit numbers and zero are palindromes
    if number < 10:
        return True

    # Convert the absolute value to string to compare characters
    # We use abs() to handle potential negative inputs robustly, 
    # though the initial check already handles negatives.
    number_str = str(abs(number))
    reversed_str = number_str[::-1]

    return number_str == reversed_str


def get_length(number: int) -> int:
    """
    Get the number of digits in a given integer.

    Args:
        number (int): The integer to measure.

    Returns:
        int: The number of digits in the integer.
    """
    # Handle zero explicitly as a special case for length calculation
    if number == 0:
        return 1

    # Count digits by converting to string and taking length
    return len(str(abs(number)))


def construct_palindrome_from_pattern(number: int, middle_suffix: str) -> int:
    """
    Construct a palindrome by mirroring a given prefix with an optional middle suffix.

    This helper is used to create potential palindrome candidates from a number
    by mirroring its left half onto the right half.

    Args:
        number (int): The source number to extract the pattern from.
        middle_suffix (str): The middle part to include (if odd length), empty string if even.

    Returns:
        int: The constructed palindrome integer.
    """
    str_num = str(number)
    length = len(str_num)

    # Determine the left half length
    if length % 2 == 0:
        left_half_len = length // 2
        right_half_len = length // 2
    else:
        left_half_len = (length - 1) // 2
        right_half_len = (length + 1) // 2

    # Extract the left half
    left_part = str_num[:left_half_len]

    # Build the mirrored part
    # If there is a middle suffix (for odd length numbers), place it in the center
    if middle_suffix:
        mirror_part = left_part + middle_suffix + left_part[::-1]
    else:
        mirror_part = left_part + left_part[::-1]

    return int(mirror_part)


def next_smallest_palindrome(number: int) -> int:
    """
    Find the next smallest palindrome strictly greater than the given number.

    This function searches for the smallest palindrome that is greater than
    the input number. It handles various edge cases including single digits,
    all-nines numbers, and negative inputs.

    Args:
        number (int): The integer to find the next palindrome for.

    Returns:
        int: The next smallest palindrome strictly greater than the input number.

    Raises:
        ValueError: If the input number is invalid (e.g., negative, though 
                     mathematically palindromes can be negative, the problem
                     context and standard convention imply positive integers).
                     However, based on typical palindrome problems, we assume 
                     non-negative inputs are expected. If negative input is provided,
                     we treat it as invalid for this specific "next smallest" logic
                     which usually applies to positive integers, OR we return the
                     smallest positive palindrome if we strictly follow mathematical 
                     palindrome definitions. 
                     Given the assertions (99->101), we assume domain is natural numbers.

    Strategy:
    1. If the input is less than the smallest 10-digit number (1000000001), 
       we can construct candidates of the same length and the next length.
    2. We start by constructing a palindrome with the same number of digits 
       by mirroring the left half of the number.
    3. If this constructed palindrome is <= the input number, we increment the 
       middle part (effectively the left half) and mirror again.
    4. If that fails (carrying over increases the length), we construct the 
       smallest palindrome of the next length (10^(n-1) + 1 for n digits, 
       e.g., 99 -> 101).
    """

    # Input validation
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, received {type(number).__name__}")

    if number < 0:
        # Based on the problem context (99->101), we expect positive integers.
        # If a negative number is passed, the "next smallest palindrome" is ambiguous 
        # without a defined lower bound. We will raise an error for clarity, 
        # treating negative numbers as outside the valid domain for this specific problem.
        raise ValueError("Input number must be non-negative.")

    # Edge case: 0
    if number == 0:
        return 1

    length = get_length(number)
    str_num = str(number)

    # Strategy 1: Try to find a palindrome of the same length
    # Start by creating a palindrome from the current number's left half.

    # Determine the split point for the middle element (if odd length)
    # For length 3 (e.g., "123"), left is "1", middle is "2", right is "3".
    # We mirror "1" to get "111".

    # Calculate the number of digits in the left half (excluding middle for odd)
    if length % 2 == 0:
        mid_point = length // 2
        left_half = str_num[:mid_point]
        right_half_len = mid_point
    else:
        mid_point = length // 2
        left_half = str_num[:mid_point]
        middle_char = str_num[mid_point]
        right_half_len = mid_point + 1

    # Case A: Even length or the middle char is not part of the prefix we mirror
    # We construct the initial candidate.

    if length % 2 == 0:
        # Even length: e.g., 1221 -> left="12", mirror -> 1221
        # e.g., 1234 -> left="12", mirror -> 1221
        candidate_prefix = left_half
        candidate = construct_palindrome_from_pattern(number, "")
    else:
        # Odd length: e.g., 12345 -> left="12", middle="3", mirror -> 12321
        # e.g., 123 -> left="1", middle="2", mirror -> 121
        candidate_prefix = left_half + middle_char
        candidate = construct_palindrome_from_pattern(number, middle_char)

    # Check if the constructed candidate is strictly greater than the number
    if candidate > number:
        return candidate

    # If not greater, we need to increment the left half and try again.
    # The left half is the integer representation of the prefix.
    prefix_int = int(candidate_prefix) if (length % 2 != 0) else int(left_half)

    # Wait, logic refinement for odd numbers:
    # If length is 3, number=129. str="129". mid_point=1. left_half="1". middle_char="2".
    # candidate_prefix should be "1" (left) + "2" (mid) = "12"? No.
    # To generate the next, we increment the 'number formed by the first (length+1)/2 digits'.

    # Let's redefine the "seed" we increment.
    # For 1221 (len 4): seed is 12. Next is 13 -> 1331.
    # For 121 (len 3): seed is 12. Next is 13 -> 131.
    # For 129 (len 3): seed is 12. Next is 13 -> 131.
    # For 1234 (len 4): seed is 12. Candidate 1221 <= 1234. Increment seed 12->13. 1331 > 1234.
    # For 9999 (len 4): seed is 99. Candidate 9999 <= 9999. Increment 99->100. 
    #    But length changes.

    # Correct Logic:
    # Take the integer formed by the first ceil(length/2) digits.
    # Increment it.
    # If the incremented number has more digits than ceil(length/2), 
    # it means we overflowed (e.g., 999 -> 1000), so we go to the next length case.

    # Re-calculate the seed length
    seed_len = (length + 1) // 2

    # Extract the seed
    seed_str = str_num[:seed_len]
    seed_int = int(seed_str)

    # Increment the seed
    next_seed_int = seed_int + 1

    # Convert back to string to check length
    next_seed_str = str(next_seed_int)

    # If the seed length increased, it means we carried over into the next magnitude
    # (e.g., 99 -> 100, or 9 -> 10).
    if len(next_seed_str) > seed_len:
        # Overflow occurred: the next palindrome must have more digits.
        # The smallest palindrome of length N+1 is 1 followed by N-1 zeros followed by 1.
        # Formula: 10^(length) + 1
        return (10 ** length) + 1
    else:
        # No overflow, use the new seed to construct the palindrome
        # We need to determine the middle char for construction if length is odd
        current_len = length

        # The new seed might have a different structure than the old one regarding the middle char
        # But since we just incremented the integer, we can just reconstruct the palindrome
        # using the new seed and the original length parity.

        if current_len % 2 == 0:
            # Even length: mirror the whole seed
            # e.g., length 4, seed 12 -> 1221
            left_part = next_seed_str
            candidate = construct_palindrome_from_pattern(0, "", left_part) # Simplified logic below handles this better

            # Actually, let's use the helper with appropriate arguments
            # Helper expects (number, middle_suffix)
            # We can just build it manually to be precise
            # left = next_seed_str
            # right = left[::-1]
            # candidate = int(left + right)

            candidate = int(next_seed_str + next_seed_str[::-1])
        else:
            # Odd length: the last digit of the seed is the middle
            # e.g., length 3, seed 12 -> 121
            # left part = all but last char of seed
            # middle = last char of seed
            # right = reverse(left)

            left_part = next_seed_str[:-1]
            middle_char = next_seed_str[-1]
            right_part = left_part[::-1]
            candidate = int(left_part + middle_char + right_part)

        return candidate


def solve_problem(number: int) -> int:
    """
    Wrapper function that encapsulates the logic for finding the next smallest palindrome.
    This serves as the primary entry point.
    """
    return next_smallest_palindrome(number)


# Re-implementing next_smallest_palindrome cleanly without local re-definitions to ensure clarity and correctness
def final_next_smallest_palindrome(number: int) -> int:
    """
    Robust implementation to find the next smallest palindrome strictly greater than number.
    """
    # Input validation
    if not isinstance(number, int):
        raise TypeError(f"Expected int, got {type(number).__name__}")

    if number < 0:
        raise ValueError("Input must be non-negative.")

    # Edge case: 0
    if number == 0:
        return 1

    s = str(number)
    n = len(s)

    # Step 1: Generate a palindrome of the same length by mirroring the first half.
    # The "first half" includes the middle digit if the length is odd.
    mid_index = n // 2

    # Extract the left half including middle (for odd lengths)
    # Example: "12345" -> mid=2, s[:3] = "123". Mirror -> "12321"
    # Example: "1234" -> mid=2, s[:2] = "12". Mirror -> "1221"
    left_part = s[:mid_index]

    if n % 2 == 1:
        # Odd length: middle char is the last char of left_part
        middle_char = left_part[-1]
        left_side = left_part[:-1]
        right_side = left_side[::-1]
        palindrome = int(left_part + middle_char + right_side)
    else:
        # Even length