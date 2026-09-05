from typing import List, Any

def _validate_input_list(data: Any) -> None:
    """
    Validates that the input is a list and not None.
    Raises a TypeError if validation fails.
    """
    if data is None:
        raise TypeError("Input cannot be None. Expected a list.")

    if not isinstance(data, list):
        raise TypeError(f"Input must be a list. Received type: {type(data).__name__}")

def _check_empty_list() -> bool:
    """
    Returns True for empty lists, as they are trivially monotonic.
    """
    return True

def _check_single_element_list() -> bool:
    """
    Returns True for lists with exactly one element, as they are trivially monotonic.
    """
    return True

def _is_strictly_increasing(indices: range, first_val: float, second_val: float) -> bool:
    """
    Checks if the pair (first_val, second_val) satisfies strictly increasing condition.
    """
    return second_val > first_val

def _is_strictly_decreasing(indices: range, first_val: float, second_val: float) -> bool:
    """
    Checks if the pair (first_val, second_val) satisfies strictly decreasing condition.
    """
    return second_val < first_val

def _is_equal(first_val: float, second_val: float) -> bool:
    """
    Checks if two values are strictly equal.
    """
    return first_val == second_val

def _check_monotonicity_consistency(current_direction: int, 
                                   prev_diff: int, 
                                   curr_diff: int) -> int:
    """
    Determines the new direction based on previous and current differences.

    Returns:
        1 if still increasing
        -1 if still decreasing
        0 if equal
        2 if direction changed (not monotonic)
    """
    # If previous direction was increasing (1) and current is not strictly increasing
    if current_direction == 1:
        if curr_diff <= 0:
            # Check if it becomes equal or decreasing
            if curr_diff < 0:
                return 2  # Change from inc to dec -> Not monotonic
            else:
                return 1  # Still equal or transitioning, stay inc check pending

        # If current is increasing, direction remains 1
        return 1

    # If previous direction was decreasing (-1) and current is not strictly decreasing
    if current_direction == -1:
        if curr_diff >= 0:
            # Check if it becomes equal or increasing
            if curr_diff > 0:
                return 2  # Change from dec to inc -> Not monotonic
            else:
                return -1 # Still equal or transitioning, stay dec check pending

        # If current is decreasing, direction remains -1
        return -1

    # If direction was neutral (0, all equal so far)
    if current_direction == 0:
        if curr_diff > 0:
            return 1  # Started increasing
        elif curr_diff < 0:
            return -1 # Started decreasing
        else:
            return 0  # Still all equal

    return 0

def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Handles:
    - Empty lists (True)
    - Single element (True)
    - All equal elements (True)
    - Strictly increasing
    - Strictly decreasing
    - Mixed/Invalid sequences (False)

    Validates input type explicitly.
    """

    # Step 1: Validate Input
    _validate_input_list(l)

    # Step 2: Handle Degenerate Cases (Empty or Single Element)
    if _check_empty_list():
        return True

    if _check_single_element_list():
        return True

    # Step 3: Initialize State Variables
    n = len(l)
    current_direction = 0  # 0: Neutral, 1: Increasing, -1: Decreasing
    prev_diff = 0
    is_monotonic_so_far = True

    # Step 4: Iterate through pairs to check relationships
    for i in range(n - 1):
        curr_val = l[i]
        next_val = l[i + 1]

        # Calculate current difference
        diff = next_val - curr_val

        # Determine current relationship direction
        if diff > 0:
            curr_dir = 1
        elif diff < 0:
            curr_dir = -1
        else:
            curr_dir = 0

        # Update state based on direction consistency
        current_direction = _check_monotonicity_consistency(
            current_direction, 
            prev_diff, 
            diff
        )

        # If direction became inconsistent (changed from inc to dec or vice versa)
        if current_direction == 2:
            is_monotonic_so_far = False
            break

        # Prepare for next iteration
        prev_diff = diff

        # Early exit optimization if already determined false
        if not is_monotonic_so_far:
            break

    return is_monotonic_so_far