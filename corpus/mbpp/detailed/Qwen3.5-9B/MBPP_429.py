from typing import Tuple, Union

# Define the type alias for a tuple of integers to ensure type safety throughout the function
TupleOfInts = Tuple[int, ...]


def _validate_input_tuple(input_tuple: Union[int, TupleOfInts, None]) -> TupleOfInts:
    """
    Validates that the provided argument is a non-empty tuple of integers.

    This helper function performs explicit checks:
    1. Checks if the input is None.
    2. Checks if the input is not a tuple.
    3. Checks if the tuple is empty.
    4. Checks if any element within the tuple is not an integer (excluding bools which are int subclass).

    Parameters:
    - input_tuple: The input to validate.

    Returns:
    - The validated tuple of integers.

    Raises:
    - TypeError: If the input is not a tuple or contains non-integer elements.
    - ValueError: If the input tuple is empty.
    """

    # Check for None explicitly first
    if input_tuple is None:
        raise TypeError("Input must be a tuple of integers, but received None.")

    # Check if the input is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Input must be a tuple of integers, but received {type(input_tuple).__name__}.")

    # Check for empty tuple (degenerate case)
    if len(input_tuple) == 0:
        raise ValueError("Input tuple cannot be empty.")

    # Iterate through elements to validate types
    for index, element in enumerate(input_tuple):
        # Explicitly check for bool because bool is a subclass of int in Python,
        # but logically we usually want strict integers.
        if isinstance(element, bool):
            raise TypeError(f"Element at index {index} is a boolean, expected an integer.")
        if not isinstance(element, int):
            raise TypeError(f"Element at index {index} is not an integer ({type(element).__name__}), expected an integer.")

    return input_tuple


def _compute_elementwise_and(tuple_a: TupleOfInts, tuple_b: TupleOfInts) -> TupleOfInts:
    """
    Computes the bitwise AND of corresponding elements in two tuples of equal length.

    This function assumes both input tuples have been validated and are of equal length
    by the caller or a preceding validation step. It uses explicit loops and named variables
    to ensure clarity and defensive programming.

    Parameters:
    - tuple_a: The first tuple of integers.
    - tuple_b: The second tuple of integers.

    Returns:
    - A new tuple containing the bitwise AND of corresponding elements.

    Raises:
    - ValueError: If the lengths of the two tuples do not match.
    """

    # Ensure lengths match before processing
    if len(tuple_a) != len(tuple_b):
        raise ValueError(
            f"Tuples must be of equal length. Length of first tuple: {len(tuple_a)}, "
            f"Length of second tuple: {len(tuple_b)}."
        )

    # Initialize an empty list to collect results
    result_list: list = []

    # Iterate over the length of the tuples (guaranteed safe as checked above)
    for i in range(len(tuple_a)):
        current_value_a = tuple_a[i]
        current_value_b = tuple_b[i]

        # Perform bitwise AND operation
        bitwise_result = current_value_a & current_value_b

        # Append result to the list
        result_list.append(bitwise_result)

    # Convert the list back to a tuple as the return type specification requires
    return tuple(result_list)


def and_tuples(tuple_a: TupleOfInts, tuple_b: TupleOfInts) -> TupleOfInts:
    """
    Extracts the elementwise bitwise AND tuples from the given two tuples.

    This is the main entry point for the operation. It handles input validation
    defensively and delegates the computation to a dedicated helper function.

    Parameters:
    - tuple_a: The first tuple of integers.
    - tuple_b: The second tuple of integers.

    Returns:
    - A tuple containing the elementwise bitwise AND of the inputs.

    Raises:
    - TypeError: If inputs are not tuples or contain invalid types.
    - ValueError: If inputs are empty or of unequal lengths.
    """

    # Step 1: Validate both input tuples explicitly
    validated_a = _validate_input_tuple(tuple_a)
    validated_b = _validate_input_tuple(tuple_b)

    # Step 2: Compute the elementwise AND using the validated, cleaned inputs
    computed_result = _compute_elementwise_and(validated_a, validated_b)

    return computed_result