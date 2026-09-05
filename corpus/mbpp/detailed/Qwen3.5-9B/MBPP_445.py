from typing import Tuple, Union, Any

def _validate_tuple_structure(first_element: Any, second_element: Any) -> bool:
    """
    Validates that two elements form a valid pair for index-wise multiplication.

    Requirements for a valid pair:
    1. Both elements must be tuples.
    2. Both elements must have the same length.
    3. Both elements must contain only numeric types (int or float).

    Returns:
        True if valid, False otherwise.
    """
    # Check if both are tuples
    if not isinstance(first_element, tuple) or not isinstance(second_element, tuple):
        return False

    # Check if lengths match
    if len(first_element) != len(second_element):
        return False

    # Check for empty tuples
    if len(first_element) == 0:
        # An empty tuple is mathematically valid for the operation (result is empty tuple)
        return True

    # Check for numeric types in the tuples
    first_len = len(first_element)
    second_len = len(second_element)

    for i in range(first_len):
        # Check first tuple
        if not isinstance(first_element[i], (int, float)):
            return False
        # Check second tuple
        if not isinstance(second_element[i], (int, float)):
            return False

    return True


def _multiply_indexed_pairs(first_pair: Tuple[Any, Any], 
                            second_pair: Tuple[Any, Any]) -> Tuple[Tuple[float, ...], ...]:
    """
    Performs element-wise multiplication on two paired tuples.

    Args:
        first_pair: A tuple containing two tuples (tuple_a, tuple_b) to be multiplied.
        second_pair: A tuple containing two tuples (tuple_c, tuple_d) to be multiplied with the above.

    Returns:
        A tuple of tuples where each inner tuple contains the multiplied values.
        Result length equals the input length.
    """
    result = []

    # Extract the pairs
    tuple_a = first_pair[0]
    tuple_b = first_pair[1]
    tuple_c = second_pair[0]
    tuple_d = second_pair[1]

    # Iterate through indices of the tuples
    for index in range(len(tuple_a)):
        # Get elements at current index
        val1 = tuple_a[index]
        val2 = tuple_b[index]
        val3 = tuple_c[index]
        val4 = tuple_d[index]

        # Perform index-wise multiplication: (val1 * val2) and (val3 * val4)
        product1 = val1 * val2
        product2 = val3 * val4

        # Create the resulting tuple pair for this index
        result_pair = (product1, product2)
        result.append(result_pair)

    return tuple(result)


def _validate_and_prepare_tuples(first_input: Any, 
                                 second_input: Any) -> Tuple[Tuple[Any, ...], Tuple[Any, ...]]:
    """
    Validates that the main inputs are structured as expected and prepares them.

    Expected structure:
    - Each input must be a tuple.
    - Each element within the input tuple must be a tuple.
    - All inner tuples in the first input must have the same length.
    - All inner tuples in the second input must have the same length.
    - The length of inner tuples in first input must match the length of inner tuples in second input.

    Returns:
        A tuple containing the validated and prepared first and second inputs.

    Raises:
        ValueError: If the input structure is invalid.
        TypeError: If the types are incorrect.
    """
    # Check if main inputs are tuples
    if not isinstance(first_input, tuple) or not isinstance(second_input, tuple):
        raise TypeError("Both inputs must be tuples.")

    if len(first_input) == 0 or len(second_input) == 0:
        # Handle empty main tuples gracefully by returning empty result handling
        pass

    # Validate each element in the main tuples
    for i, element in enumerate(first_input):
        if not isinstance(element, tuple):
            raise TypeError(f"Element at index {i} in first input must be a tuple.")

    for i, element in enumerate(second_input):
        if not isinstance(element, tuple):
            raise TypeError(f"Element at index {i} in second input must be a tuple.")

    # Get the length of the inner tuples from the first element
    first_inner_length = 0
    second_inner_length = 0

    if len(first_input) > 0:
        first_inner_length = len(first_input[0])
        if first_inner_length != len(first_input[1]):
             # Check consistency across all elements in first input
             for elem in first_input:
                 if len(elem) != first_inner_length:
                     raise ValueError(f"All inner tuples in the first input must have the same length.")
    else:
        # If input is empty, we assume 0 length consistency holds trivially
        pass

    if len(second_input) > 0:
        second_inner_length = len(second_input[0])
        if second_inner_length != len(second_input[1]):
             for elem in second_input:
                 if len(elem) != second_inner_length:
                     raise ValueError(f"All inner tuples in the second input must have the same length.")
    else:
        pass

    # Check if lengths of inner tuples match between the two main tuples
    if first_inner_length != second_inner_length and (len(first_input) > 0 and len(second_input) > 0):
        raise ValueError(f"Inner tuples in first input (length {first_inner_length}) must have the same length as inner tuples in second input (length {second_inner_length}).")

    # Additional pairwise validation for each index pair
    total_pairs = len(first_input)

    if total_pairs != len(second_input):
        raise ValueError(f"Both inputs must have the same number of elements. Got {total_pairs} vs {len(second_input)}.")

    for index in range(total_pairs):
        pair_tuple_1 = first_input[index]
        pair_tuple_2 = second_input[index]

        if not _validate_tuple_structure(pair_tuple_1, pair_tuple_2):
            raise ValueError(f"Invalid structure at index {index}.")

    return first_input, second_input


def index_multiplication(first_input: Tuple[Tuple[Any, ...], ...], 
                         second_input: Tuple[Tuple[Any, ...], ...]) -> Tuple[Tuple[float, ...], ...]:
    """
    Performs index-wise multiplication of tuple elements in the given two tuples.

    For each index i, takes the i-th tuple from the first input (A_i) and the i-th tuple 
    from the second input (B_i).
    Then, computes a new tuple C_i where:
        C_i[0] = A_i[0] * B_i[0]
        C_i[1] = A_i[1] * B_i[1]
        ...

    This is essentially performing matrix multiplication where the matrices are 2xN 
    and resulting in a 2xN structure, but element-wise for each column.

    Args:
        first_input: A tuple of tuples, where each inner tuple represents a row of numbers.
                     Example: ((a, b), (c, d), (e, f)) represents a 2x3 structure.
        second_input: Another tuple of tuples with the same structure.

    Returns:
        A tuple of tuples representing the result of index-wise multiplication.
        The structure matches the input dimensions.

    Raises:
        TypeError: If inputs are not tuples or contain non-tuple elements.
        ValueError: If structures are inconsistent (e.g., mismatched lengths).

    Example:
        >>> index_multiplication(((1, 3), (4, 5)), ((6, 7), (3, 9)))
        ((6, 21), (12, 45))
    """
    # Step 1: Validate and prepare inputs
    prepared_first, prepared_second = _validate_and_prepare_tuples(first_input, second_input)

    # Step 2: Perform the multiplication logic
    result = _multiply_indexed_pairs(prepared_first, prepared_second)

    return result