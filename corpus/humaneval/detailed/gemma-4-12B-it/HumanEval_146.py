from typing import List, Union

def is_odd(digit: int) -> bool:
    """Checks if a single digit is odd (1, 3, 5, 7, 9)."""
    return digit % 2 != 0

def get_first_and_last_digits(number: int) -> (int, int):
    """
    Extracts the first and last digits of an integer.
    The sign of the number is ignored for digit extraction.
    """
    # Use absolute value to ignore negative signs
    absolute_value = abs(number)

    # Convert to string to easily access digits
    str_representation = str(absolute_value)

    # Extract digits
    # Note: For single digit numbers, first and last digits are the same.
    first_digit = int(str_representation[0])
    last_digit = int(str_representation[-1])

    return first_digit, last_digit

def is_special_number(n: Union[int, float]) -> bool:
    """
    Determines if a number meets the criteria:
    1. It is strictly greater than 10.
    2. Its first digit is odd.
    3. Its last digit is odd.
    """
    # Requirement 1: Must be greater than 10
    if n <= 10:
        return False

    # Ensure we are working with an integer for digit extraction
    # The problem context implies integer digits, so we cast or treat as int.
    # If float, we truncate or treat the integer part.
    integer_part = int(n)

    # Extra safety check: if n was 10.5, it is > 10 but int(10.5) is 10.
    # The problem asks for "numbers", usually implying the value itself.
    # We use the integer part of the actual value provided.
    if integer_part <= 10 and n > 10:
        # This handles cases like 10.5 where the integer part is 10.
        # However, the prompt's examples suggest integers.
        # Let's stick to the value comparison first.
        pass

    first_digit, last_digit = get_first_and_last_digits(integer_part)

    first_is_odd = is_odd(first_digit)
    last_is_odd = is_odd(last_digit)

    return first_is_odd and last_is_odd

def specialFilter(nums: List[Union[int, float]]) -> int:
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Validation: Ensure input is a list
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers.")

    count = 0

    # Iterate through every number in the input list
    for item in nums:
        # Validate that the current item is a number
        if not isinstance(item, (int, float)):
            # Production-grade code should decide whether to skip or raise.
            # Given the signature, we skip invalid types to maintain robustness.
            continue

        # Check the conditions using the helper function
        if is_special_number(item):
            count += 1

    return count