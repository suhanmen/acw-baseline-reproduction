from typing import List, Union

def _validate_input_types(l: list, t: int) -> None:
    """
    Validates that the input list contains only numbers (int or float)
    and that the threshold is a number.

    Raises TypeError if validation fails.
    """
    # Validate the threshold type
    if not isinstance(t, (int, float)):
        raise TypeError(f"Threshold must be a number, got {type(t).__name__}")

    # Validate the list contents
    for index, item in enumerate(l):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements in the list must be numbers. "
                f"Found {type(item).__name__} at index {index}."
            )

def _is_single_element_below_threshold(value: Union[int, float], threshold: Union[int, float]) -> bool:
    """
    Checks if a single value is strictly less than the threshold.
    """
    is_below = value < threshold
    return is_below

def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Step 1: Validate the input types to ensure production-grade stability
    _validate_input_types(l, t)

    # Step 2: Handle the edge case of an empty list.
    # Conventionally, "all" of an empty set satisfies a condition (Vacuous truth).
    if len(l) == 0:
        return True

    # Step 3: Iterate through the list and check each element.
    # We use an explicit loop to ensure clarity and easy debugging.
    for index, current_value in enumerate(l):
        # Determine if the current element violates the rule
        is_valid_element = _is_single_element_below_threshold(current_value, t)

        if not is_valid_element:
            # If any element is found to be equal to or greater than the 
            # threshold, we immediately return False.
            return False

    # Step 4: If the loop completes without returning False, all elements 
    # were strictly below the threshold.
    return True