from typing import List, Any


def is_integer_type(item: Any) -> bool:
    """
    Checks if an item is strictly of the integer type.

    Note: This logic excludes booleans because in Python, 
    bool is a subclass of int, but typically in these contexts,
    we want only actual integers.

    Args:
        item: The object to check.

    Returns:
        True if the item is an integer and not a boolean, False otherwise.
    """
    # We check for bool first because isinstance(True, int) is True.
    # Usually, "count integers" in a heterogeneous list implies 
    # types like 1, 2, 3, not True/False.
    if isinstance(item, bool):
        return False

    if isinstance(item, int):
        return True

    return False


def count_integer(input_list: List[Any]) -> int:
    """
    Counts the number of elements in a list that are of the integer type.

    This function is defensive: it handles non-list inputs by raising a 
    TypeError and ensures that floats like 1.0 are not counted as integers 
    unless they are strictly represented as int types in the list.

    Args:
        input_list: A list containing various types of data.

    Returns:
        int: The total count of integers found in the list.

    Raises:
        TypeError: If the input provided is not a list.
    """
    # Input Validation
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input type 'list', but received '{type(input_list).__name__}'")

    # Handle the edge case of an empty list explicitly
    if len(input_list) == 0:
        return 0

    integer_count = 0

    # Iterate through every element to check its type
    for index, element in enumerate(input_list):
        # We use a helper function to determine if the element is an integer
        is_valid_int = is_integer_type(element)

        if is_valid_int:
            integer_count += 1
        else:
            # Explicitly skip non-integer types (strings, floats, None, etc.)
            continue

    return integer_count


if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt.
    assert count_integer([1, 2, 'abc', 1.2]) == 2
    assert count_integer([1, 2, 3]) == 3
    assert count_integer([1, 1.2, 4, 5.1]) == 2

    # Additional defensive edge cases
    assert count_integer([]) == 0
    assert count_integer([True, False]) == 0  # Booleans are ints in Python, but usually not wanted
    assert count_integer([0, -1, 100]) == 3
    assert count_integer([None, "1", 5.0]) == 0