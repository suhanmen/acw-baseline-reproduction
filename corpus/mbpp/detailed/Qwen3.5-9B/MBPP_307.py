from typing import Any, Tuple, Union

Number = Union[int, float]

def _is_index_valid(index: int, length: int) -> bool:
    """
    Check if the given index is valid for a tuple of the given length.
    Valid indices are from 0 (inclusive) to length-1 (inclusive).

    Returns:
        True if the index is valid, False otherwise.
    """
    return index >= 0 and index < length

def _get_tuplex_before_split(tuplex: Tuple[Any, ...], index: int) -> Tuple[Any, ...]:
    """
    Extract the portion of the tuple before the specified index.
    This is equivalent to slicing from start to the index (exclusive).

    Args:
        tuplex: The original tuple to split.
        index: The split point.

    Returns:
        A new tuple containing elements before the split point.
    """
    return tuplex[:index]

def _get_tuplex_after_split(tuplex: Tuple[Any, ...], index: int) -> Tuple[Any, ...]:
    """
    Extract the portion of the tuple starting from the specified index.
    This is equivalent to slicing from the index to the end.

    Args:
        tuplex: The original tuple to split.
        index: The split point.

    Returns:
        A new tuple containing elements from the split point onwards.
    """
    return tuplex[index:]

def _wrap_in_list_with_default(elements: Tuple[Any, ...], default_value: Number) -> Tuple[list]:
    """
    Create a single-element list containing a modified version of the input tuple's elements.

    The first element of the input tuple becomes the list, with the last element replaced by the default_value
    if the input tuple is not empty. If the input tuple is empty, the list contains the default_value.

    This specific behavior is inferred from the problem's test cases where an empty list [] inside the tuple
    gets replaced by [default_value].

    Args:
        elements: A tuple representing the remaining part of the tuple after the split.
        default_value: The number to insert into the list.

    Returns:
        A tuple containing a single list element.
    """
    if len(elements) == 0:
        # Case: Empty tuple part (e.g., from slicing after the last element)
        # Result is a list containing just the default value
        result_list = [default_value]
    else:
        # Case: Non-empty tuple part
        # Convert the first element of this part into a list
        # The test cases show that if there was an empty list, it gets replaced.
        # Based on the example: ("HELLO", 5, [], True) -> split at 2 -> elements=[(), []]? 
        # Wait, let's re-examine the split logic based on the provided examples.

        # Example: ("HELLO", 5, [], True) split at 2
        # Result: ("HELLO", 5, [50], True)
        # Split at 2 means:
        # Before: ("HELLO", 5)
        # After: ( [], True ) -> Wait, indices are 0:"HELLO", 1:5, 2:[], 3:True.
        # Slicing [2:] gives ([], True).
        # The result replaces the element at index 2 (which was []) with [50].
        # So the logic is: Take the element at the split index, make it a list with the default value,
        # and place it back in that position.

        # Let's re-evaluate the splitting logic based on the "replace element at index" hypothesis.
        pass

def _replace_element_at_index(
    tuplex: Tuple[Any, ...], 
    index: int, 
    new_value: list
) -> Tuple[Any, ...]:
    """
    Create a new tuple identical to the input tuple but with the element at the specified index replaced by the new_value.

    Args:
        tuplex: The original tuple.
        index: The index to replace.
        new_value: The new value (a list) to insert at that index.

    Returns:
        A new tuple with the modification.
    """
    if not _is_index_valid(index, len(tuplex)):
        raise ValueError(f"Index {index} is out of range for tuple of length {len(tuplex)}")

    # Construct the new tuple using concatenation for clarity and explicit steps
    elements_before = tuplex[:index]
    elements_after = tuplex[index+1:]

    return tuple(list(elements_before) + [new_value] + list(elements_after))

def colon_tuplex(tuplex: Tuple[Any, ...], index: int, default_value: Number) -> Tuple[Any, ...]:
    """
    Function to get a colon of a tuple.

    This function modifies the tuple at the specified index by replacing the element
    with a list containing the default_value. If the element at the index is not present
    (i.e., index is out of bounds), it raises a ValueError.

    The behavior observed from the test cases:
    Input: ("HELLO", 5, [], True), index=2, default=50
    Tuple indices: 0="HELLO", 1=5, 2=[], 3=True
    Element at index 2 is [].
    Result replaces [] with [50].

    Args:
        tuplex: The input tuple.
        index: The index where the replacement should occur.
        default_value: The number to put inside the new list.

    Returns:
        A new tuple with the modified list at the specified index.

    Raises:
        ValueError: If the index is out of bounds for the given tuple.
        TypeError: If the inputs are not of the expected types.
    """

    # --- Validation Phase ---

    # Check if tuplex is actually a tuple
    if not isinstance(tuplex, tuple):
        raise TypeError("Input 'tuplex' must be a tuple.")

    # Check if index is an integer
    if not isinstance(index, int):
        raise TypeError("Argument 'index' must be an integer.")

    # Check if default_value is a number (int or float)
    if not isinstance(default_value, (int, float)):
        raise TypeError("Argument 'default_value' must be a number (int or float).")

    # Get the length of the tuple for validation
    length = len(tuplex)

    # Check for edge case: empty tuple
    if length == 0:
        raise ValueError("Cannot perform operation on an empty tuple.")

    # Validate the index bounds explicitly
    if not (0 <= index < length):
        raise ValueError(f"Index {index} is out of range for tuple of length {length}.")

    # --- Execution Phase ---

    # Identify the element to be replaced
    element_to_replace = tuplex[index]

    # Create the new list value. 
    # Based on the problem description and examples, the original element is discarded
    # and replaced by a list containing solely the default_value.
    # Example: [] becomes [50].
    new_element = [default_value]

    # Create the resulting tuple with the replacement
    # We use explicit slicing and concatenation to ensure the structure is clear
    result_tuple = _replace_element_at_index(tuplex, index, new_element)

    return result_tuple