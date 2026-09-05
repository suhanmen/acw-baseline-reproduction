from typing import List, Tuple, Any, Union

def add_lists(input_list: List[Any], input_tuple: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Takes a list and a tuple and returns a new tuple containing the 
    elements of the input_tuple followed by the elements of the input_list.

    Args:
        input_list (List[Any]): A list of elements to append.
        input_tuple (Tuple[Any, ...]): A tuple of elements to prefix.

    Returns:
        Tuple[Any, ...]: A concatenated tuple.

    Raises:
        TypeError: If input_list is not a list or input_tuple is not a tuple.
        ValueError: If either input is None.
    """
    # --- Input Validation ---

    # Check for None values explicitly
    if input_list is None:
        raise ValueError("The input_list parameter cannot be None.")
    if input_tuple is None:
        raise ValueError("The input_tuple parameter cannot be None.")

    # Validate types to ensure production-grade robustness
    if not isinstance(input_list, list):
        raise TypeError(
            f"Expected input_list to be of type 'list', "
            f"but received '{type(input_list).__name__}'."
        )

    if not isinstance(input_tuple, tuple):
        raise TypeError(
            f"Expected input_tuple to be of type 'tuple', "
            f"but received '{type(input_tuple).__name__}'."
        )

    # --- Logic Implementation ---

    # Handle edge case: empty list
    # If the list is empty, the result is just the original tuple.
    if len(input_list) == 0:
        return input_tuple

    # Handle edge case: empty tuple
    # If the tuple is empty, the result is the list converted to a tuple.
    if len(input_tuple) == 0:
        return tuple(input_list)

    # Convert the list into a tuple to prepare for concatenation.
    # This ensures we are working with homogeneous types for the final result.
    list_as_tuple: Tuple[Any, ...] = tuple(input_list)

    # Concatenate the original tuple with the new tuple created from the list.
    # In Python, the '+' operator on tuples creates a new tuple.
    result_tuple: Tuple[Any, ...] = input_tuple + list_as_tuple

    return result_tuple

if __name__ == "__main__":
    # These assertions verify the requirements provided in the problem description.
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)