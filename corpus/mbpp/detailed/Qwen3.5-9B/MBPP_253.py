from typing import List, Any

def is_integer_value(value: Any) -> bool:
    """
    Determines if the given value is effectively an integer.

    This function handles various edge cases:
    - Standard integers (int): True
    - Floats that are whole numbers (e.g., 4.0): True
    - Floats with fractional parts (e.g., 4.1): False
    - Non-numeric types (str, None, etc.): False

    Args:
        value: The value to check.

    Returns:
        True if the value represents an integer, False otherwise.
    """
    # First, check if the value is an integer instance
    if isinstance(value, int):
        # Explicitly exclude booleans, as bool is a subclass of int in Python
        if isinstance(value, bool):
            return False
        return True

    # Check for floating point numbers
    if isinstance(value, float):
        # Use the method defined in Python's float documentation
        # value.is_integer() returns True if the value is a whole number
        return value.is_integer()

    # Reject all other types including strings, None, lists, etc.
    return False


def count_integer(input_list: Any) -> int:
    """
    Counts the number of integer values in the given list.

    This function performs the following steps:
    1. Validates that the input is a list.
    2. Iterates through each element in the list.
    3. Checks if each element is an integer value using the helper function.
    4. Accumulates the count of valid integers.
    5. Returns the final count.

    Edge cases handled:
    - Empty list: Returns 0.
    - List with non-integer elements: Counts only the integers.
    - List with mixed types: Handles safely without raising errors.
    - List with zero, negative numbers: Correctly identifies them as integers.
    - List with boolean values: Correctly excludes them (treated as non-integers here).
    - List with floats that are whole numbers (e.g., 4.0): Includes them.

    Args:
        input_list: A list of mixed type elements to count integers from.

    Returns:
        The count of integer values in the list.

    Raises:
        TypeError: If the input is not a list.
    """
    # Validate the input type explicitly
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but received {type(input_list).__name__}")

    # Initialize the counter variable to zero
    count = 0

    # Iterate over each element in the list
    for element in input_list:
        # Check if the current element is an integer value
        if is_integer_value(element):
            # Increment the counter if it is an integer
            count = count + 1

    # Return the final count
    return count