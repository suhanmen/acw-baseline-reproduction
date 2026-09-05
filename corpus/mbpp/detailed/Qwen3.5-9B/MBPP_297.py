from typing import Any, List, Union

FlattenedResult = List[Any]
NestedInput = Union[Any, List[Any]]

def _is_iterable(item: Any) -> bool:
    """
    Determine if an item is an iterable list for the purposes of flattening.

    We explicitly exclude strings and bytes to prevent characters/bytes 
    from being treated as individual elements, as is standard practice.
    """
    if item is None:
        return False
    if isinstance(item, (str, bytes)):
        return False
    return isinstance(item, list)

def _flatten_recursive(element: NestedInput, accumulator: List[Any]) -> None:
    """
    Recursively flatten a nested structure.

    - If the element is a list, iterate through its items and recursively flatten each one.
    - If the element is not a list, append it directly to the accumulator.
    """
    current_element = element
    acc = accumulator

    if _is_iterable(current_element):
        # Case: The element is a nested list
        for sub_item in current_element:
            _flatten_recursive(sub_item, acc)
    else:
        # Case: The element is a leaf value (number, string, etc.)
        acc.append(current_element)

def flatten_list(nested_structure: NestedInput) -> FlattenedResult:
    """
    Flatten a nested list structure into a single-level list.

    This function handles arbitrary levels of nesting.
    It explicitly validates inputs to ensure they are lists as expected.
    It handles edge cases such as empty lists, lists containing non-lists,
    and deeply nested structures.

    Args:
        nested_structure: A potentially nested list of arbitrary depth.

    Returns:
        A flattened list containing all atomic elements from the input.

    Raises:
        TypeError: If the input is not a list.
    """
    # Input validation: Ensure the top-level input is a list
    if nested_structure is None:
        raise TypeError("Input cannot be None. Expected a list.")

    if not isinstance(nested_structure, list):
        raise TypeError(f"Input must be a list. Received type: {type(nested_structure).__name__}")

    # Initialize the accumulator list
    result_list: List[Any] = []

    # Begin the recursive flattening process
    _flatten_recursive(nested_structure, result_list)

    return result_list