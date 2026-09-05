from typing import Tuple, Any

def validate_input(tuple_a: Any, tuple_b: Any) -> Tuple[Tuple[Any, ...], Tuple[Any, ...]]:
    """
    Validates that both inputs are tuples and returns them as-is if valid.
    Raises a TypeError if either input is not a tuple.
    """
    if not isinstance(tuple_a, tuple):
        raise TypeError(f"First argument must be a tuple, got {type(tuple_a).__name__}")
    if not isinstance(tuple_b, tuple):
        raise TypeError(f"Second argument must be a tuple, got {type(tuple_b).__name__}")

    return tuple_a, tuple_b

def validate_lengths(tuple_a: Tuple[Any, ...], tuple_b: Tuple[Any, ...]) -> bool:
    """
    Validates that both tuples have the same length.
    Returns True if valid, False otherwise.
    """
    if len(tuple_a) != len(tuple_b):
        return False
    return True

def substract_tuple_elements(
    tuple_a: Tuple[Any, ...], 
    tuple_b: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    """
    Subtracts corresponding elements of tuple_b from tuple_a.
    Returns a new tuple containing the results.

    Steps:
    1. Initialize an empty list to store results.
    2. Iterate over both tuples simultaneously using zip().
    3. For each pair of elements (a, b), compute (a - b).
    4. Convert the list of results back to a tuple.
    """
    result_list = []

    for a, b in zip(tuple_a, tuple_b):
        difference = a - b
        result_list.append(difference)

    return tuple(result_list)

def substract_elements(tuple_a: Any, tuple_b: Any) -> Tuple[Any, ...]:
    """
    Main function to subtract corresponding elements of two tuples.

    Edge cases handled:
    - Empty tuples: Returns an empty tuple.
    - Single element tuples: Works correctly.
    - All-equal elements: Returns a tuple of zeros.
    - Negative numbers: Handled correctly by subtraction.
    - Invalid input types: Raises TypeError with a descriptive message.
    - Unequal lengths: Raises ValueError with a descriptive message.

    Parameters:
    tuple_a (Any): The first tuple.
    tuple_b (Any): The second tuple.

    Returns:
    Tuple[Any, ...]: A new tuple containing the subtracted values.

    Raises:
    TypeError: If either input is not a tuple.
    ValueError: If the tuples have different lengths.
    """
    # Step 1: Validate input types
    validated_tuple_a, validated_tuple_b = validate_input(tuple_a, tuple_b)

    # Step 2: Validate input lengths
    if not validate_lengths(validated_tuple_a, validated_tuple_b):
        raise ValueError(f"Tuples must have the same length. Got {len(validated_tuple_a)} and {len(validated_tuple_b)}")

    # Step 3: Perform the subtraction
    result = substract_tuple_elements(validated_tuple_a, validated_tuple_b)

    return result