import math
from typing import List, Union

Number = Union[int, float]


def _is_valid_number(value: object) -> bool:
    """
    Check if the given object is an instance of int or float.

    Args:
        value: The object to check.

    Returns:
        True if the value is a valid number (int or float), False otherwise.
    """
    return isinstance(value, (int, float))


def _validate_input_list(lst: object) -> List[Number]:
    """
    Validate that the input is a list and all elements are valid numbers.

    Args:
        lst: The input object to validate.

    Returns:
        The original list if valid.

    Raises:
        TypeError: If the input is not a list or contains invalid elements.
    """
    if not isinstance(lst, list):
        raise TypeError(f"Input must be a list, got {type(lst).__name__} instead.")

    validated_list = []
    for i, item in enumerate(lst):
        if not _is_valid_number(item):
            raise TypeError(f"Element at index {i} is not a number: {item!r} ({type(item).__name__}).")
        validated_list.append(item)

    return validated_list


def _round_up_to_int(value: Number) -> int:
    """
    Round a number up to the nearest integer (ceiling).

    This function handles:
    - Positive floats: rounds up (e.g., 1.4 -> 2)
    - Negative floats: rounds up towards positive infinity (e.g., -2.4 -> -2)
    - Integers: returns the integer itself

    Args:
        value: A number (int or float) to round up.

    Returns:
        The smallest integer greater than or equal to the value.
    """
    return math.ceil(value)


def _square_number(number: int) -> int:
    """
    Calculate the square of a number.

    Args:
        number: The number to square.

    Returns:
        The square of the number.
    """
    return number * number


def _sum_squares(numbers: List[int]) -> int:
    """
    Calculate the sum of squares for a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of the squares of all integers in the list.
    """
    total = 0
    for num in numbers:
        total = total + _square_number(num)
    return total


def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6

    """
    # Step 1: Validate the input list structure and contents
    validated_input_list = _validate_input_list(lst)

    # Step 2: Transform each number by rounding it up to the nearest integer
    rounded_numbers = []
    for original_value in validated_input_list:
        rounded_value = _round_up_to_int(original_value)
        rounded_numbers.append(rounded_value)

    # Step 3: Calculate the square of each rounded number
    squared_numbers = []
    for rounded_number in rounded_numbers:
        squared_value = _square_number(rounded_number)
        squared_numbers.append(squared_value)

    # Step 4: Sum all the squared values
    final_sum = _sum_squares(squared_numbers)

    return final_sum