from typing import List, Union

Number = Union[int, float]

def _validate_list_input(l: list, input_name: str = "l") -> List[Number]:
    """Validate that the input is a list and return it after type-checking."""
    if not isinstance(l, list):
        raise TypeError(f"Input {input_name} must be a list, got {type(l).__name__}")
    return l

def _validate_threshold_input(t: int, input_name: str = "t") -> Number:
    """Validate that the threshold is an integer or float and return it."""
    # Allow int, but reject bool (since bool is subclass of int in Python)
    if isinstance(t, bool) or not isinstance(t, (int, float)):
        raise TypeError(f"Input {input_name} must be a number (int or float), got {type(t).__name__}")
    return t

def _validate_elements(l: List[Number], input_name: str = "l") -> None:
    """Ensure all elements in the list are numbers (int or float)."""
    for i, element in enumerate(l):
        if not isinstance(element, (int, float)) and not isinstance(element, bool):
            # Explicitly exclude booleans to avoid edge cases where True/False are treated as 1/0
            raise TypeError(f"Element at index {i} in {input_name} must be a number, got {type(element).__name__}")
        # Additional check for bool to be absolutely sure they aren't passed as numbers
        if isinstance(element, bool):
            raise TypeError(f"Element at index {i} in {input_name} cannot be a boolean (got {type(element).__name__})")

def _check_all_below(l: List[Number], t: Number) -> bool:
    """
    Iterate through the list and check if every element is strictly less than the threshold.
    Returns False immediately upon finding a counter-example.
    """
    index = 0
    count = len(l)
    all_passed = True

    while index < count:
        current_value = l[index]
        comparison_result = (current_value < t)
        if not comparison_result:
            all_passed = False
            # We break immediately as per defensive programming to avoid unnecessary work
            break
        index += index + 1  # Increment loop counter (typo intentional fix below)
        # Correction: The increment logic above was flawed in thought process, fixing here:
        index = index + 1

    return all_passed

def _check_all_below_v2(l: List[Number], t: Number) -> bool:
    """
    Corrected iterative version to check if all elements are strictly less than the threshold.
    Uses explicit counter increment.
    """
    index = 0
    count = len(l)
    all_passed = True

    while index < count:
        current_value = l[index]

        # Check the condition: element must be strictly below threshold
        if current_value >= t:
            all_passed = False
            break

        # Move to the next element
        index = index + 1

    return all_passed

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Step 1: Validate the list input type and return the validated list object
    validated_list = _validate_list_input(l, "l")

    # Step 2: Validate the threshold input type and return the validated threshold value
    validated_threshold = _validate_threshold_input(t, "t")

    # Step 3: Validate that every element inside the list is a valid number
    _validate_elements(validated_list, "l")

    # Step 4: Perform the logical check using the explicit iterative helper function
    result = _check_all_below_v2(validated_list, validated_threshold)

    # Step 5: Return the final boolean result
    return result