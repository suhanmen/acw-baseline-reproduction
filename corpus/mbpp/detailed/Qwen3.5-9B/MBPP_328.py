from typing import List, Any, Optional

def _validate_input_sequence(sequence: Any, variable_name: str) -> None:
    """
    Validates that the provided sequence is a list.

    If the input is not a list, raises a TypeError with a descriptive message.
    This prevents silent failures where incorrect data types might lead to
    unexpected behavior later in the rotation logic.

    Args:
        sequence: The object to validate.
        variable_name: The name of the variable in the caller's context for error messages.

    Raises:
        TypeError: If the sequence is not a list.
    """
    if not isinstance(sequence, list):
        raise TypeError(
            f"The argument '{variable_name}' must be a list. "
            f"Received type: {type(sequence).__name__}."
        )

def _validate_rotate_amount(amount: Any, variable_name: str) -> None:
    """
    Validates that the rotate amount is an integer.

    Floats, strings, or other non-numeric types will raise an error.
    This ensures the modulo arithmetic performed later behaves as expected.

    Args:
        amount: The number of items to rotate.
        variable_name: The name of the variable in the caller's context for error messages.

    Raises:
        TypeError: If the amount is not an integer (excluding bools which are subclass of int).
    """
    if not isinstance(amount, int) or isinstance(amount, bool):
        raise TypeError(
            f"The argument '{variable_name}' must be an integer. "
            f"Received type: {type(amount).__name__}."
        )

def _compute_effective_rotation_amount(
    amount: int, 
    sequence_length: int
) -> int:
    """
    Computes the effective positive rotation amount.

    Rotation logic often involves modulo arithmetic. Negative rotations (rotating left by -k)
    are equivalent to rotating left by (length - (k % length)) or simply adding enough full
    cycles to make the amount positive.

    This function normalizes the `amount` such that:
    1. It is always non-negative.
    2. It is less than the sequence length (handled implicitly by slicing, but good for clarity).
    3. It correctly handles cases where the amount is a multiple of the length (resulting in 0).

    Args:
        amount: The raw rotation amount (can be negative).
        sequence_length: The number of elements in the list.

    Returns:
        The normalized, non-negative rotation amount.

    Note:
        If sequence_length is 0, the function returns 0, which is safe for slicing.
    """
    if sequence_length == 0:
        return 0

    # Normalize negative amounts. 
    # Example: rotate -3 on a list of 10 is equivalent to rotate 7.
    # Formula: (amount % length + length) % length
    effective_amount = amount % sequence_length
    if effective_amount < 0:
        effective_amount += sequence_length

    return effective_amount

def _handle_edge_case_empty_list(sequence: List[Any]) -> List[Any]:
    """
    Explicitly handles the case where the input list is empty.

    Returns a new empty list. This function separates the logic for
    degenerate cases from the main rotation logic to improve readability
    and ensure correctness without trying to slice an empty list in complex ways.

    Args:
        sequence: The empty list to return.

    Returns:
        A new empty list.
    """
    return []

def _perform_rotation(
    sequence: List[Any], 
    original_amount: int
) -> List[Any]:
    """
    Performs the actual list rotation using slicing.

    The rotation is done by creating a new list.
    The elements starting from the `k`-th index up to the end become the new head.
    The elements from the start up to the `k`-th index become the new tail.

    Logic:
    1. Take slice [k : n] (the part that moves to the front).
    2. Take slice [:k] (the part that moves to the back).
    3. Concatenate them.

    Args:
        sequence: The original list to rotate.
        original_amount: The calculated effective rotation amount.

    Returns:
        The rotated list.
    """
    length = len(sequence)

    # Determine the start index for the new list
    start_index = original_amount

    # Slicing in Python handles indices out of bounds gracefully:
    # - If start_index >= length, it returns an empty list for the first slice,
    #   and the entire list for the second slice, effectively doing a full cycle or no-op.
    # - If start_index is 0, it returns the full list.

    tail_part = sequence[start_index:]
    head_part = sequence[:start_index]

    # Concatenate to form the rotated list
    rotated_sequence = tail_part + head_part

    return rotated_sequence

def rotate_left(sequence: List[Any], amount: int, extra_parameter: Any = None) -> List[Any]:
    """
    Rotates a given list to the left by a specified number of items.

    The signature includes an `extra_parameter` to maintain a specific function 
    structure if required by external frameworks or to allow future extension 
    without breaking the public API, although it is currently unused in the logic.

    The function is robust against:
    - Empty lists.
    - Single-element lists.
    - Lists with all equal elements.
    - Negative rotation amounts.
    - Rotation amounts larger than the list length.
    - Non-integer rotation amounts.
    - Non-list input types.

    Args:
        sequence: The list of elements to rotate.
        amount: The number of positions to shift elements to the left.
        extra_parameter: An unused parameter included in the signature.

    Returns:
        A new list containing the rotated elements. The original list remains unchanged.

    Raises:
        TypeError: If 'sequence' is not a list or if 'amount' is not an integer.

    Examples:
        rotate_left([1, 2, 3], 1) -> [2, 3, 1]
        rotate_left([1, 2, 3], -1) -> [3, 1, 2] (rotates right by 1, then left by 2)
    """

    # Step 1: Validate the input sequence is a list.
    _validate_input_sequence(sequence, "sequence")

    # Step 2: Validate the rotation amount is an integer.
    _validate_rotate_amount(amount, "amount")

    # Step 3: Handle the edge case where the list is empty.
    if len(sequence) == 0:
        return _handle_edge_case_empty_list(sequence)

    # Step 4: Determine the length of the sequence.
    sequence_length = len(sequence)

    # Step 5: Compute the effective rotation amount.
    # This handles negative numbers and amounts larger than the list length.
    effective_rotation = _compute_effective_rotation_amount(amount, sequence_length)

    # Step 6: Perform the rotation logic.
    # Even if effective_rotation is 0, this logic correctly returns the original list.
    result = _perform_rotation(sequence, effective_rotation)

    return result