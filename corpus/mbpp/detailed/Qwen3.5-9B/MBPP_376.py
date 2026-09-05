from collections import Counter
from typing import Tuple, Any, Dict

def _get_element_counts(input_tuple: Tuple[Any, ...]) -> Dict[Any, int]:
    """
    Helper function to count the occurrences of each element in the input tuple.

    Args:
        input_tuple: The tuple of elements to count.

    Returns:
        A dictionary where keys are elements from the tuple and values are their counts.
    """
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Expected a tuple, but got {type(input_tuple).__name__}")

    counts_dict = dict(Counter(input_tuple))
    return counts_dict

def _identify_duplicate_elements(counts_dict: Dict[Any, int]) -> set:
    """
    Helper function to identify which elements appear more than once.

    Args:
        counts_dict: A dictionary of element counts.

    Returns:
        A set containing elements that have a count greater than 1.
    """
    duplicates = set()
    for element, count in counts_dict.items():
        if count > 1:
            duplicates.add(element)
    return duplicates

def _process_element(element: Any, is_duplicate: bool, replacement_value: str) -> Any:
    """
    Helper function to determine the final value of an element based on whether it is a duplicate.

    Args:
        element: The current element being processed.
        is_duplicate: Boolean indicating if the element is considered a duplicate.
        replacement_value: The value to replace duplicates with.

    Returns:
        The element if it is not a duplicate, or the replacement value if it is.
    """
    if is_duplicate:
        return replacement_value
    return element

def remove_replica(input_tuple: Tuple[Any, ...], replacement_value: str = 'MSP') -> Tuple[Any, ...]:
    """
    Removes tuple elements that occur more than once by replacing them with a custom value.

    This function iterates through the input tuple, identifies elements that appear more 
    than once, and replaces all occurrences of those elements with the provided replacement 
    value. Elements that appear exactly once are kept as is.

    Args:
        input_tuple: A tuple of elements. Can contain any hashable type.
        replacement_value: The value to replace duplicate elements with. Defaults to 'MSP'.

    Returns:
        A new tuple with duplicate elements replaced by the replacement_value.

    Raises:
        TypeError: If the input is not a tuple.
    """
    # Validate input type immediately
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple, got {type(input_tuple).__name__}")

    # Handle the edge case of an empty tuple explicitly
    if len(input_tuple) == 0:
        return tuple()

    # Step 1: Count occurrences of each element
    element_counts = _get_element_counts(input_tuple)

    # Step 2: Identify which elements are duplicates (count > 1)
    duplicate_elements = _identify_duplicate_elements(element_counts)

    # Step 3: Construct the result tuple
    result_list = []
    for item in input_tuple:
        # Check if the current item is in our set of duplicate elements
        if item in duplicate_elements:
            processed_item = _process_element(item, True, replacement_value)
        else:
            processed_item = _process_element(item, False, replacement_value)
        result_list.append(processed_item)

    # Convert the list back to a tuple before returning
    return tuple(result_list)