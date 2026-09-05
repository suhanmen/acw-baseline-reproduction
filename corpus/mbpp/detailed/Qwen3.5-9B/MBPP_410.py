from typing import Any, Union, Tuple

Number = Union[int, float]

def _is_comparable_with_number(value: Any) -> bool:
    """
    Determine if a value can be meaningfully compared with numbers.
    We consider strings as comparable only if they look like numbers
    (e.g., '42', '3.14'), but the problem implies strings like 'Python'
    should be ignored or treated as non-comparable, leading to an error.
    Based on the problem's context where mixed types exist but the min
    is a number, we will treat non-numeric types (unless they are numeric strings)
    as causing an explicit error to maintain type safety and clarity.
    """
    if isinstance(value, (int, float)):
        # Exclude booleans as they are technically ints in Python but semantically different
        if isinstance(value, bool):
            return False
        return True

    if isinstance(value, str):
        try:
            float(value)
            return True
        except ValueError:
            return False

    return False

def _extract_numeric_values(items: list) -> list:
    """
    Filters the input list to keep only elements that can be numerically compared.
    Returns a new list containing only those valid numeric-like values.
    """
    filtered_values = []
    for item in items:
        if _is_comparable_with_number(item):
            filtered_values.append(item)
        # If an item is not comparable, it is simply skipped in this extraction phase.
        # However, the problem implies we must find a min. If no numbers exist,
        # we should handle that explicitly later.
    return filtered_values

def _find_minimum_value(numeric_list: list) -> Number:
    """
    Finds the minimum value in a list of guaranteed numeric values.
    Handles edge cases like empty lists by raising a ValueError.
    """
    if not numeric_list:
        raise ValueError("No numeric values found in the input to determine a minimum.")

    # Initialize the minimum with the first element
    current_minimum = numeric_list[0]

    # Iterate through the rest of the list starting from the second element
    for i in range(1, len(numeric_list)):
        candidate_value = numeric_list[i]

        # Explicit comparison step
        if candidate_value < current_minimum:
            current_minimum = candidate_value

    return current_minimum

def min_val(data: list) -> Number:
    """
    Finds the minimum numeric value in a given heterogeneous list.

    Behavior:
    - Iterates through the list to find elements comparable with numbers.
    - Validates that at least one numeric value exists.
    - Explicitly handles edge cases (empty list, all non-numeric).
    - Returns the smallest numeric value found.

    Args:
        data (list): A list containing mixed types (strings, numbers, etc.).

    Returns:
        Number: The minimum numeric value found in the list.

    Raises:
        ValueError: If the list is empty or contains no comparable numeric values.
        TypeError: If an unexpected type is encountered that cannot be processed.
    """
    # Step 1: Validate the input type
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    # Step 2: Handle the empty list case explicitly
    if len(data) == 0:
        raise ValueError("Input list is empty; cannot determine a minimum value.")

    # Step 3: Extract valid numeric values from the heterogeneous list
    valid_numerics = _extract_numeric_values(data)

    # Step 4: Check if any valid numeric values were found
    if len(valid_numerics) == 0:
        raise ValueError("Input list contains no values comparable with numbers.")

    # Step 5: Find and return the minimum among the valid numerics
    result = _find_minimum_value(valid_numerics)

    return result