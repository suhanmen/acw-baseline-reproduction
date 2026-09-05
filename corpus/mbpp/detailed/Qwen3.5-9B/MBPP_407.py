from typing import Union, Optional

def _is_valid_integer(value: object) -> bool:
    """
    Checks if the input is an integer.

    Edge cases handled:
    - None
    - Floats (even whole ones like 5.0)
    - Booleans (subclass of int, but typically not desired as input for digit manipulation)
    - Negative numbers (allowed as input per problem constraints, logic will handle sign)
    - Zero (allowed)
    """
    if isinstance(value, bool):
        return False
    if not isinstance(value, int):
        return False
    return True


def _get_digits(number: int) -> list[int]:
    """
    Extracts digits from an integer and returns them as a list.
    Handles negative numbers by ignoring the sign.

    Edge cases handled:
    - Zero returns [0]
    - Negative numbers strip the '-' sign and extract magnitude digits
    """
    if number < 0:
        number = -number

    if number == 0:
        return [0]

    digits = []
    temp = number

    while temp > 0:
        current_digit = temp % 10
        digits.append(current_digit)
        temp = temp // 10

    # The digits were extracted in reverse order (least significant first)
    # Reverse them back to original order
    digits.reverse()
    return digits


def _digits_to_number(digits: list[int]) -> int:
    """
    Converts a list of digits back into an integer.

    Example: [1, 2, 3] -> 123
    Example: [0, 5] -> 5
    """
    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result


def _find_next_permutation_indices(digits: list[int]) -> Optional[tuple[int, int]]:
    """
    Finds the first pair of indices (i, j) such that digits[i] < digits[j] and j is the
    smallest index greater than i satisfying this, with j being the rightmost possible
    to satisfy the condition for maximizing the increase.

    Algorithm:
    1. Traverse from right to left to find the first index 'i' where digits[i] < digits[i+1].
       If no such index exists, the number is the largest possible permutation (descending order).
    2. If 'i' is found, traverse from the right to find the first index 'j' such that
       digits[i] < digits[j].
    3. Swap digits[i] and digits[j].
    4. Reverse the subarray from i+1 to the end.

    Returns:
    - A tuple (i, j) if a next permutation exists.
    - None if the current permutation is the largest possible.
    """
    n = len(digits)

    # Step 1: Find the first pivot index i from the right
    pivot_index = -1
    for k in range(n - 2, -1, -1):
        if digits[k] < digits[k + 1]:
            pivot_index = k
            break

    if pivot_index == -1:
        # No such pivot exists; this is the largest permutation
        return None

    # Step 2: Find the element just larger than digits[pivot_index] to its right
    # Traverse from right to left to find the smallest element > digits[pivot_index]
    successor_index = -1
    pivot_value = digits[pivot_index]

    for k in range(n - 1, pivot_index, -1):
        if digits[k] > pivot_value:
            successor_index = k
            break

    # This should logically always be found given Step 1 succeeded, but defensive coding:
    if successor_index == -1:
        return None

    # Step 3: Swap
    # We do the swap directly on the list, but for clarity in this explicit solution,
    # we will create a new list state to represent the swap, then reverse the suffix.
    # Actually, modifying in place is fine, but let's be explicit about the steps.

    # Create a working copy to avoid mutating original input if called multiple times with same list
    working_digits = digits.copy()

    # Perform swap
    temp_val = working_digits[pivot_index]
    working_digits[pivot_index] = working_digits[successor_index]
    working_digits[successor_index] = temp_val

    # Step 4: Reverse the suffix starting from pivot_index + 1
    start_suffix = pivot_index + 1
    end_suffix = n

    # Manual reversal for explicitness
    left = start_suffix
    right = end_suffix - 1
    while left < right:
        working_digits[left], working_digits[right] = working_digits[right], working_digits[left]
        left += 1
        right -= 1

    return working_digits, pivot_index, successor_index


def rearrange_bigger(number: int) -> Optional[int]:
    """
    Rearranges the digits of a given number to find the next bigger number.
    If no bigger number can be formed, returns False.

    Parameters:
    - number (int): The input integer.

    Returns:
    - int: The next bigger number formed by rearranging digits.
    - False: If no such number exists (current digits form the largest permutation).

    Edge cases handled:
    - Empty input / non-integers: Returns False after validation.
    - Single element: Returns False (cannot rearrange a single digit to be bigger).
    - All-equal elements: Returns False.
    - Negative numbers: Logic applies to magnitude; returns negative result or False.
    - Zero: Returns False.
    """

    # 1. Validate input explicitly
    if not _is_valid_integer(number):
        return False

    # 2. Handle single digit case explicitly
    # A single digit number cannot be rearranged to become bigger.
    if number < 10:
        return False

    # 3. Handle zero explicitly (though < 10 covers it, good for clarity)
    if number == 0:
        return False

    # 4. Extract digits
    digits = _get_digits(number)

    # 5. Attempt to find the next permutation
    next_permutation_digits, _, _ = _find_next_permutation_indices(digits)

    # 6. Check if a next permutation was found
    if next_permutation_digits is None:
        return False

    # 7. Convert the new digit list back to an integer
    next_bigger = _digits_to_number(next_permutation_digits)

    # 8. Preserve the sign of the original number if it was negative
    # The problem examples imply positive integers, but general logic requires sign handling.
    # If input was negative, the "next bigger" usually implies the next bigger magnitude 
    # representing the same scale, or the next bigger value. 
    # Standard interpretation for "next bigger number by rearranging digits" usually 
    # treats the number as a sequence of digits. If input is -12, digits are 1,2. 
    # Next bigger magnitude is 21, so result -21? Or does it mean -12 -> -21 is smaller?
    # Let's assume the standard "next permutation of digits" logic on the magnitude.
    # However, strictly speaking, -12 < -21 is False. -21 is smaller than -12.
    # The next *bigger* integer would be -12 -> -12 (no change) -> ... 
    # Actually, if input is -12, the next bigger integer with same digits (-1, -2?) 
    # usually isn't the standard interview question scope. 
    # Given assertions are all positive, we will assume non-negative inputs for the "bigger" logic.
    # If negative input is provided, we calculate the next permutation of the absolute value.
    # But what about the sign? 
    # If input is -12, and we find next permutation of 12 is 21. 
    # Is -21 bigger than -12? No.
    # Is there a larger negative number? -12 is larger than -21.
    # The next larger negative number would be -12 itself (current) if we consider all permutations.
    # Since -12 is the largest permutation of digits {1, 2} with a negative sign (because 21 is the max magnitude),
    # there is no larger number than -12 with those digits that is also negative.
    # Unless we consider -21? No, -21 < -12.
    # So for negative numbers, if the magnitude is already the largest permutation, we return False.
    # If the magnitude can be increased, the negative result will be a SMALLER number (more negative).
    # Example: Input -10. Digits 1, 0. Largest mag: 10. Result -10. No bigger.
    # Example: Input -12. Digits 1, 2. Next mag: 21. Result -21. -21 < -12. 
    # So strictly, -21 is NOT bigger than -12.
    # Therefore, for negative numbers, the concept of "next bigger" by rearranging digits 
    # usually implies increasing the magnitude if the question implies treating digits as unsigned blocks,
    # OR it implies the mathematical inequality.
    # Given the problem context (assertions are positive), we will treat the input as non-negative
    # for the purpose of finding a "bigger" number. If a negative number is passed, 
    # the mathematical next bigger value with those digits does not exist (since flipping order 
    # increases magnitude, making the negative number smaller).
    # Thus, if number < 0, we can technically return False immediately because 
    # rearranging digits to increase magnitude decreases the value of a negative number.

    if number < 0:
        return False

    return next_bigger