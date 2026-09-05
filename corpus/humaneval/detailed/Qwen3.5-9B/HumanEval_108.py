from typing import List, Union

Number = Union[int, float]


def _extract_signed_digits(number: int) -> List[int]:
    """
    Extracts the signed digits of an integer according to the problem rules:
    - Positive numbers: standard digits (e.g., 123 -> [1, 2, 3])
    - Negative numbers: first digit is negative, rest are positive (e.g., -123 -> [-1, 2, 3])
    - Zero: returns an empty list as per the logic (sum of digits would be 0 anyway)

    Args:
        number (int): An integer to extract signed digits from.

    Returns:
        List[int]: A list of integers representing the signed digits.
    """
    # Convert number to string for digit extraction
    number_str = str(number)

    # If the number is zero, there are no digits to sum to get > 0
    if number == 0:
        return []

    digits = []

    # Process the first character
    if number_str[0] == '-':
        # For negative numbers, the first digit is negative
        first_digit = int(number_str[1])
        digits.append(-first_digit)

        # Process remaining characters (which are positive digits)
        for char in number_str[2:]:
            digits.append(int(char))
    else:
        # For positive numbers, all digits are positive
        for char in number_str:
            digits.append(int(char))

    return digits


def _calculate_digit_sum(digits: List[int]) -> int:
    """
    Calculates the sum of the given list of digits.

    Args:
        digits (List[int]): A list of integers representing digits.

    Returns:
        int: The sum of the digits.
    """
    total = 0
    for digit in digits:
        total += digit
    return total


def count_nums(arr: List[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.

    Args:
        arr (List[int]): A list of integers.

    Returns:
        int: The count of elements where the sum of their signed digits is greater than 0.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers.")

    # Validate individual elements
    for item in arr:
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers. Found: {type(item).__name__}")

    count = 0

    for number in arr:
        # Extract signed digits
        signed_digits = _extract_signed_digits(number)

        # Calculate the sum of these digits
        digit_sum = _calculate_digit_sum(signed_digits)

        # Check if the sum is greater than 0
        if digit_sum > 0:
            count += 1

    return count