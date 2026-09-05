from typing import Tuple, List

def and_tuples(tuple1: Tuple[int, ...], tuple2: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    Extracts the result of a bitwise AND operation between corresponding elements
    of two tuples.

    The function validates that the inputs are tuples, contain only integers,
    and are of equal length. If any validation fails, it raises a ValueError.

    Args:
        tuple1: A tuple of integers.
        tuple2: A tuple of integers.

    Returns:
        A tuple containing the bitwise AND of corresponding elements.

    Raises:
        ValueError: If inputs are not tuples, have different lengths, 
                    or contain non-integer elements.
    """
    # --- Input Validation ---

    # Check if both inputs are actually instances of tuple
    if not isinstance(tuple1, tuple):
        raise ValueError(f"First argument must be a tuple, got {type(tuple1).__name__}")

    if not isinstance(tuple2, tuple):
        raise ValueError(f"Second argument must be a tuple, got {type(tuple2).__name__}")

    # Check if the tuples have the same length
    length1 = len(tuple1)
    length2 = len(tuple2)

    if length1 != length2:
        raise ValueError(
            f"Tuples must have the same length. Received lengths: {length1} and {length2}"
        )

    # Check if all elements in both tuples are integers
    # This ensures robust behavior for mixed-type inputs
    for i, val in enumerate(tuple1):
        if not isinstance(val, int):
            raise ValueError(f"Element at index {i} in first tuple is not an integer: {val}")

    for i, val in enumerate(tuple2):
        if not isinstance(val, int):
            raise ValueError(f"Element at index {i} in second tuple is not an integer: {val}")

    # --- Processing Logic ---

    # Handle the empty tuple edge case explicitly
    if length1 == 0:
        return ()

    # Initialize a list to store the results
    # We use a list because tuples are immutable and we need to build the collection
    results: List[int] = []

    # Iterate through the indices of the tuples
    for index in range(length1):
        # Extract the elements from the current position
        value_from_tuple1 = tuple1[index]
        value_from_tuple2 = tuple2[index]

        # Perform the bitwise AND operation
        # Example: 10 (1010) & 5 (0101) = 0 (0000)
        # Example: 11 (1011) & 14 (1110) = 10 (1010)
        bitwise_and_result = value_from_tuple1 & value_from_tuple2

        # Append the result to our working list
        results.append(bitwise_and_result)

    # Convert the list of results back into a tuple to match the required return type
    final_result_tuple = tuple(results)

    return final_result_tuple