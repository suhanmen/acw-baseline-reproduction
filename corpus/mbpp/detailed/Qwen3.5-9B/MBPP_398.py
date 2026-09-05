from typing import Any, List, Union

def _is_numeric(value: Any) -> bool:
    """
    Check if the given value is numeric (int or float).

    Args:
        value: The value to check.

    Returns:
        True if value is an int or float, False otherwise.
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def _sum_digits_of_integer(n: int) -> int:
    """
    Compute the sum of digits of an integer.
    Handles negative numbers by summing the absolute values of digits.

    Args:
        n: The integer whose digits are to be summed.

    Returns:
        The sum of the digits.
    """
    if n < 0:
        n = -n

    if n == 0:
        return 0

    digit_sum = 0
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        digit_sum += digit
        temp_n = temp_n // 10

    return digit_sum

def sum_of_digits(list_of_values: List[Any]) -> Union[int, None]:
    """
    Compute the sum of digits of each number in the given list and return the total sum.

    Args:
        list_of_values: A list of values. Numeric values will have their digits summed,
                        non-numeric values will be skipped.

    Returns:
        The total sum of all digit sums found in the list.
        Returns None if the input list is None.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains invalid nested structures (e.g., non-iterable inside that isn't None).
    """
    if list_of_values is None:
        return None

    if not isinstance(list_of_values, list):
        raise TypeError("Input must be a list of values.")

    if len(list_of_values) == 0:
        return 0

    total_sum = 0

    for item in list_of_values:
        if isinstance(item, list):
            raise ValueError("List elements must be atomic values (numbers) or single non-list items.")

        if _is_numeric(item):
            numeric_value = int(item)
            digit_sum = _sum_digits_of_integer(numeric_value)
            total_sum += digit_sum

    return total_sum