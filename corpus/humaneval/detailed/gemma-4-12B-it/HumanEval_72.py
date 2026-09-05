from typing import List, Any

def is_palindromic(sequence: List[Any]) -> bool:
    """
    Helper function to check if a list is palindromic.
    A sequence is palindromic if it reads the same forwards and backwards.
    """
    if not isinstance(sequence, list):
        raise TypeError("Input 'q' must be a list.")

    # An empty list or a single element list is technically palindromic.
    if len(sequence) <= 1:
        return True

    # Compare the list with its reverse.
    # We use a loop-based comparison to be explicit.
    list_length = len(sequence)
    for i in range(list_length // 2):
        left_element = sequence[i]
        right_element = sequence[list_length - 1 - i]

        if left_element != right_element:
            return False

    return True

def calculate_total_weight(sequence: List[Any]) -> float:
    """
    Helper function to calculate the sum of elements in the list.
    Validates that all elements are numeric.
    """
    if not isinstance(sequence, list):
        raise TypeError("Input 'q' must be a list.")

    total = 0
    for item in sequence:
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in 'q' must be numbers, found: {type(item)}")
        total += item
    return float(total)

def will_it_fly(q: List[Any], w: float) -> bool:
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    # --- Input Validation ---
    # Ensure q is a list.
    if not isinstance(q, list):
        raise TypeError("The object 'q' must be a list.")

    # Ensure w is a numeric type (int or float).
    if not isinstance(w, (int, float)):
        raise TypeError("The maximum weight 'w' must be an integer or a float.")

    # --- Logic Step 1: Check Balance ---
    # The object must be a palindrome to be "balanced".
    is_balanced = is_palindromic(q)

    if not is_balanced:
        # If it's not balanced, it cannot fly regardless of weight.
        return False

    # --- Logic Step 2: Check Weight ---
    # Calculate the sum of all elements in the list.
    try:
        total_weight = calculate_total_weight(q)
    except ValueError as e:
        # Re-raise or handle cases where list contains non-numeric items.
        raise ValueError(f"Weight calculation failed: {e}")

    # The object flies if total weight <= maximum weight w.
    is_under_weight_limit = total_weight <= w

    if is_under_weight_limit:
        # It is both balanced and under weight limit.
        return True
    else:
        # It is balanced but too heavy.
        return False