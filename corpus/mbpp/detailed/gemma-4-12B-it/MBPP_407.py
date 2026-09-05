from typing import Union


def rearrange_bigger(num: int) -> Union[int, bool]:
    """
    Rearranges the digits of a given number to find the smallest number
    that is strictly greater than the original number.

    Returns:
        - The next bigger number as an integer.
        - False if no such number can be formed by rearranging the digits.
    """
    # --- Input Validation ---
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")

    if num < 0:
        # The problem context usually implies non-negative integers.
        # We treat negative numbers as having no "bigger" rearrangement 
        # relative to the magnitude logic, or handle as invalid.
        return False

    # Convert number to a list of digits for easier manipulation
    digits = list(map(int, str(num)))
    n = len(digits)

    if n == 0:
        return False

    # To find the next bigger number, we use an algorithm similar to 
    # finding the next lexicographical permutation.

    # Step 1: Find the first digit (from right to left) that is 
    # smaller than the digit to its immediate right.
    # This identifies the pivot point where the "descending" order breaks.
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            pivot_index = i
            break

    # If no such pivot exists, the digits are in non-increasing order 
    # (e.g., 321, 111, 5). No larger permutation is possible.
    if pivot_index == -1:
        return False

    # Step 2: Find the smallest digit to the right of the pivot 
    # that is strictly greater than the digit at the pivot.
    # This will be our replacement to keep the number as small as possible.
    successor_index = -1
    for j in range(n - 1, pivot_index, -1):
        if digits[j] > digits[pivot_index]:
            successor_index = j
            break

    # If we found a pivot but no successor, it shouldn't happen 
    # logically based on how pivot_index was selected, but we check for safety.
    if successor_index == -1:
        return False

    # Step 3: Swap the pivot with the successor.
    # This makes the number larger than the original.
    digits[pivot_index], digits[successor_index] = (
        digits[successor_index], 
        digits[pivot_index]
    )

    # Step 4: Since we want the smallest possible "bigger" number, 
    # the digits to the right of the pivot_index must be in 
    # ascending order (smallest to largest).
    # We sort the slice starting from pivot_index + 1 to the end.
    right_part = digits[pivot_index + 1:]
    right_part.sort()

    # Reconstruct the digits list
    result_digits = (
        digits[:pivot_index + 1] + 
        right_part
    )

    # Step 5: Convert the list of digits back to an integer.
    # We convert to string first to handle leading zeros correctly 
    # (though a leading zero only occurs if the result is 0, which 
    # shouldn't happen here as we are looking for a bigger number).
    result_str = "".join(map(str, result_digits))
    result_int = int(result_str)

    # Final check: ensure the result is actually bigger (defensive check)
    if result_int > num:
        return result_int
    else:
        return False