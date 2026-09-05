from typing import List, Any, Union

def _validate_input_list(l: Any) -> None:
    """
    Validates that the input is a list and contains comparable elements.
    Raises TypeError if the input is not a list.
    """
    if not isinstance(l, list):
        raise TypeError(f"Input must be a list, but received {type(l).__name__}.")

def _is_empty(l: list) -> bool:
    """Checks if the list is empty."""
    return len(l) == 0

def max_element(l: list) -> Union[int, float, None]:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Step 1: Validate input type
    _validate_input_list(l)

    # Step 2: Handle edge case of an empty list
    # According to standard Python behavior for max(), an empty sequence 
    # usually raises a ValueError. However, to be robust, we check explicitly.
    if _is_empty(l):
        # Returning None or raising a ValueError are common choices.
        # Given the docstring doesn't specify, we return None to avoid 
        # crashing but could also raise ValueError("max() arg is an empty sequence")
        return None

    # Step 3: Handle single element list
    if len(l) == 1:
        return l[0]

    # Step 4: Iterate and find maximum
    # We initialize the current_max with the first element of the list.
    # This ensures we handle negative numbers and zeros correctly.
    current_max = l[0]

    # We start iterating from the second element (index 1)
    for index in range(1, len(l)):
        current_item = l[index]

        # Defensive check: ensure elements are comparable
        try:
            is_greater = current_item > current_max
        except TypeError as exc:
            raise TypeError(
                f"Inconsistent types in list at index {index}: "
                f"cannot compare {type(current_item).__name__} with "
                f"{type(current_max).__name__}."
            ) from exc

        if is_greater:
            current_max = current_item

    # Step 5: Return the final result
    return current_max