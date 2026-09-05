from typing import Tuple, Union

Number = int
TupleOfNumbers = Tuple[Number, ...]
TupleOfTuples = Tuple[TupleOfNumbers, TupleOfNumbers]

def _validate_tuple_of_numbers(value: object, expected_type_name: str = "tuple of numbers") -> TupleOfNumbers:
    """
    Validates that the input is a tuple containing only integer values.
    Raises a TypeError with a descriptive message if validation fails.
    """
    if not isinstance(value, tuple):
        raise TypeError(
            f"The argument must be a tuple, but got {type(value).__name__} "
            f"instead of {expected_type_name}."
        )

    for index, item in enumerate(value):
        if not isinstance(item, int):
            raise TypeError(
                f"All elements within the tuple must be integers. "
                f"Found type {type(item).__name__} at index {index} (value: {item!r})."
            )

    return value

def _validate_tuple_pair(t1: TupleOfNumbers, t2: TupleOfNumbers) -> None:
    """
    Validates that the two tuples have the same length.
    Raises a ValueError with a descriptive message if lengths differ.
    """
    length1 = len(t1)
    length2 = len(t2)

    if length1 != length2:
        raise ValueError(
            f"Tuples must have the same length to perform element-wise XOR. "
            f"First tuple has length {length1}, second tuple has length {length2}."
        )

def _perform_single_xor_operation(a: int, b: int) -> int:
    """
    Performs the bitwise XOR operation on two individual integer values.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of a ^ b.
    """
    return a ^ b

def _perform_element_wise_xor(tuple_a: TupleOfNumbers, tuple_b: TupleOfNumbers) -> TupleOfNumbers:
    """
    Iterates through two validated tuples of the same length and performs
    the bitwise XOR operation on corresponding elements.

    Args:
        tuple_a (TupleOfNumbers): The first input tuple.
        tuple_b (TupleOfNumbers): The second input tuple.

    Returns:
        TupleOfNumbers: A new tuple containing the XOR results.
    """
    result_list = []

    # Explicitly iterate by index to ensure alignment and visibility of steps
    for index in range(len(tuple_a)):
        current_element_a = tuple_a[index]
        current_element_b = tuple_b[index]

        # Perform the operation
        xor_result = _perform_single_xor_operation(current_element_a, current_element_b)

        result_list.append(xor_result)

    # Convert the list back to a tuple for the final return type
    return tuple(result_list)

def bitwise_xor(tuple_a: TupleOfNumbers, tuple_b: TupleOfNumbers) -> TupleOfNumbers:
    """
    Performs element-wise bitwise XOR across two tuples of integers.

    This function validates the inputs to ensure they are tuples of integers
    and that both tuples have the same length. It then computes the XOR
    operation for each pair of corresponding elements.

    Args:
        tuple_a (TupleOfNumbers): The first tuple of integers.
        tuple_b (TupleOfNumbers): The second tuple of integers.

    Returns:
        TupleOfNumbers: A tuple containing the results of the XOR operations.

    Raises:
        TypeError: If inputs are not tuples or contain non-integer elements.
        ValueError: If the two tuples have different lengths.
    """
    # Step 1: Validate individual tuples and types
    validated_tuple_a = _validate_tuple_of_numbers(tuple_a)
    validated_tuple_b = _validate_tuple_of_numbers(tuple_b)

    # Step 2: Validate structural compatibility (lengths)
    _validate_tuple_pair(validated_tuple_a, validated_tuple_b)

    # Step 3: Perform the computation
    final_result = _perform_element_wise_xor(validated_tuple_a, validated_tuple_b)

    return final_result