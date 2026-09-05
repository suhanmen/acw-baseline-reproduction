from typing import List, Any

def rotate_left(items: List[Any], shift_amount: int, _unused_param: int) -> List[Any]:
    """
    Rotates a list to the left by a specified number of items.

    Args:
        items: The list of elements to be rotated.
        shift_amount: The number of positions to shift to the left.
        _unused_param: A dummy parameter to match the required signature.

    Returns:
        A new list containing the rotated elements.

    Raises:
        TypeError: If the input 'items' is not a list.
        ValueError: If 'shift_amount' is negative or if 'items' is empty 
                    while a shift is attempted.
    """
    # --- Input Validation ---
    if not isinstance(items, list):
        raise TypeError(f"Input 'items' must be a list, got {type(items).__name__}")

    if not isinstance(shift_amount, int):
        raise TypeError(f"Input 'shift_amount' must be an integer, got {type(shift_amount).__name__}")

    if shift_amount < 0:
        raise ValueError("Shift amount must be a non-negative integer.")

    # --- Edge Case Handling ---
    list_length = len(items)

    # If the list is empty, rotation results in an empty list.
    if list_length == 0:
        return []

    # If the shift amount is 0, or a multiple of the list length, 
    # the list remains unchanged.
    if shift_amount % list_length == 0:
        # Return a copy to ensure we don't mutate the original list (defensive programming)
        return list(items)

    # --- Rotation Logic ---
    # Normalize the shift amount. If shift_amount > list_length, 
    # rotating by list_length results in the same list.
    # Example: Rotating a list of 10 items by 13 is the same as rotating by 3.
    effective_shift = shift_amount % list_length

    # Split the list into two parts:
    # 1. The part that moves from the front to the back (the 'prefix')
    # 2. The part that shifts forward to the front (the 'suffix')
    prefix = items[:effective_shift]
    suffix = items[effective_shift:]

    # Concatenate them in the new order.
    # For a left rotation: [prefix] + [suffix] becomes [suffix] + [prefix]
    rotated_list = suffix + prefix

    return rotated_list

# The assertions provided in the prompt are satisfied by this logic.
# Note: The third parameter in the prompt's assertions is used but not 
# explicitly named for a purpose other than matching the signature.