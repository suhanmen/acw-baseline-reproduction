from typing import List, Union

Number = Union[int, float]

def _is_balanced(seq: List[Number]) -> bool:
    """
    Determine if the given sequence is a palindrome (balanced).

    A sequence is balanced if it reads the same forward and backward.
    This function performs an explicit character-by-character comparison
    from both ends moving toward the center.

    Args:
        seq: A list of numbers.

    Returns:
        True if the sequence is a palindrome, False otherwise.
    """
    length = len(seq)

    # An empty list is considered balanced by standard palindrome definitions
    if length == 0:
        return True

    # We only need to check up to the middle of the list
    half_length = length // 2

    for i in range(half_length):
        index_from_start = i
        index_from_end = length - 1 - i

        value_from_start = seq[index_from_start]
        value_from_end = seq[index_from_end]

        if value_from_start != value_from_end:
            return False

    return True

def _calculate_total_weight(elements: List[Number]) -> Number:
    """
    Calculate the sum of all elements in the list.

    Args:
        elements: A list of numbers.

    Returns:
        The sum of the elements.
    """
    total = 0.0
    for item in elements:
        total = total + item
    return total

def _validate_weight(w: Number) -> None:
    """
    Validate that the weight parameter is a number.

    Args:
        w: The weight value to validate.

    Raises:
        TypeError: If w is not a number.
    """
    if not isinstance(w, (int, float)):
        raise TypeError(f"Weight parameter must be a number, got {type(w).__name__}")

def _validate_load(q: List) -> None:
    """
    Validate that the load parameter is a list of numbers.

    Args:
        q: The load list to validate.

    Raises:
        TypeError: If q is not a list.
        ValueError: If q contains non-numeric elements.
    """
    if not isinstance(q, list):
        raise TypeError(f"Load parameter must be a list, got {type(q).__name__}")

    for i, item in enumerate(q):
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in the load list must be numbers. Element at index {i} is {type(item).__name__}")

def will_it_fly(q: List[Number], w: Number) -> bool:
    """
    Determine if an object will fly based on balance and weight constraints.

    The object q will fly if:
    1. It is balanced (the list is a palindrome).
    2. The sum of its elements is less than or equal to the maximum weight w.

    Args:
        q: A list representing the load of the object.
        w: The maximum possible weight the object can handle.

    Returns:
        True if the object will fly, False otherwise.

    Raises:
        TypeError: If inputs are of incorrect types.
        ValueError: If the load list contains non-numeric values.
    """
    # Step 1: Validate inputs to ensure type safety
    _validate_load(q)
    _validate_weight(w)

    # Step 2: Check if the load is balanced (palindromic)
    is_balanced_flag = _is_balanced(q)

    # Step 3: Calculate the total weight of the object
    current_weight_sum = _calculate_total_weight(q)

    # Step 4: Determine if the weight constraint is satisfied
    weight_satisfied_flag = current_weight_sum <= w

    # Step 5: Return True only if BOTH conditions are met
    return is_balanced_flag and weight_satisfied_flag