from typing import List

def get_sum_of_signed_digits(n: int) -> int:
    """
    Calculates the sum of digits of an integer. 
    If the number is negative, the first digit (the one representing 
    the magnitude of the leading digit) is treated as negative.

    Example:
    -123 -> digits are -1, 2, 3 -> sum = 4
    -11  -> digits are -1, 1  -> sum = 0
    11   -> digits are 1, 1   -> sum = 2
    """
    # Handle the zero case explicitly
    if n == 0:
        return 0

    is_negative = n < 0
    # Work with the absolute value to extract digits
    absolute_value = abs(n)

    digits = []
    temp_val = absolute_value

    # Extract digits from right to left
    while temp_val > 0:
        digit = temp_val % 10
        digits.append(digit)
        temp_val //= 10

    # The list 'digits' is currently in reverse order (units, tens, etc.)
    # However, for summing, order does not matter.

    # If the original number was negative, the first digit (most significant)
    # is treated as negative.
    # Let's find the most significant digit.
    if not digits:
        return 0

    # In our list 'digits', the last element appended is the most significant digit.
    # e.g., for 123, digits is [3, 2, 1]. Index -1 is 1.
    most_significant_digit = digits[-1]

    # Adjust the most significant digit if the original number was negative
    if is_negative:
        most_significant_digit = -most_significant_digit

    # Replace the last element in the list with the signed version
    digits[-1] = most_significant_digit

    # Sum all components
    total_sum = 0
    for d in digits:
        total_sum += d

    return total_sum

def count_nums(arr: List[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    # Defensive check: ensure the input is actually a list (or list-like)
    if not isinstance(arr, list):
        # If it's an iterable but not a list, we could convert it, 
        # but for strict production code, we check type.
        raise TypeError("Input must be a list of integers.")

    count_of_positive_sums = 0

    for element in arr:
        # Validate that each element is an integer
        if not isinstance(element, int):
            raise ValueError(f"All elements in the array must be integers. Found: {type(element)}")

        # Calculate the sum of signed digits
        current_sum = get_sum_of_signed_digits(element)

        # Check the condition specified in the problem
        if current_sum > 0:
            count_of_positive_sums += 1

    return count_of_positive_sums