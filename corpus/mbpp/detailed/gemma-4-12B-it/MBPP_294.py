from typing import List, Any, Union

def max_val(items: List[Any]) -> Union[int, float, None]:
    """
    Finds the maximum numeric value in a heterogeneous list.
    Non-numeric types (like strings, None, etc.) are ignored.

    Args:
        items (List[Any]): A list containing various data types.

    Returns:
        Union[int, float, None]: The maximum numeric value found, 
                                   or None if no numeric values exist.
    """
    # Input Validation: Ensure the input is actually a list
    if not isinstance(items, list):
        raise TypeError(f"Expected input of type 'list', but got {type(items).__name__}")

    # Handle the edge case of an empty input list
    if len(items) == 0:
        return None

    # Intermediate storage for numeric values found in the heterogeneous list
    numeric_values: List[Union[int, float]] = []

    for element in items:
        # We check if the element is an int or a float.
        # Note: We use 'isinstance' instead of 'type' to support subclasses,
        # and we explicitly exclude 'bool' because bools are instances of int 
        # in Python (True == 1, False == 0).
        is_numeric = isinstance(element, (int, float))
        is_not_boolean = not isinstance(element, bool)

        if is_numeric and is_not_boolean:
            numeric_values.append(element)

    # Handle the edge case where the list exists but contains no numeric values
    if not numeric_values:
        return None

    # Find the maximum value from the gathered numeric list
    # We initialize max_found with the first element to handle negative numbers correctly.
    max_found = numeric_values[0]

    # We skip the first element since it is already assigned to max_found
    for i in range(1, len(numeric_values)):
        current_val = numeric_values[i]
        if current_val > max_found:
            max_found = current_val

    return max_found

if __name__ == "__main__":
    # Validating provided assertions
    assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
    assert max_val(['Python', 15, 20, 25]) == 25
    assert max_val(['Python', 30, 20, 40, 50, 'version']) == 50

    # Additional defensive checks
    assert max_val([]) is None
    assert max_val(['a', 'b', 'c']) is None
    assert max_val([True, False, 10]) == 10
    assert max_val([-10, -20, -5]) == -5
    assert max_val([1.5, 2.8, 2.1]) == 2.8