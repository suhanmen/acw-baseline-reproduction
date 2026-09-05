from typing import Tuple, Any

def _validate_nested_tuple_structure(nested_tuple: Tuple[Tuple[Any, ...], ...]) -> None:
    """
    Validates that the input is a tuple of tuples and that all inner 
    tuples have the same length.
    """
    if not isinstance(nested_tuple, tuple):
        raise TypeError(f"Expected a tuple, but got {type(nested_tuple).__name__}")

    if len(nested_tuple) == 0:
        return

    first_inner_len = len(nested_tuple[0])
    if not isinstance(nested_tuple[0], tuple):
        raise TypeError("Elements of the outer tuple must be tuples.")

    for i, inner_tuple in enumerate(nested_tuple):
        if not isinstance(inner_tuple, tuple):
            raise TypeError(f"Element at index {i} is not a tuple.")
        if len(inner_tuple) != first_inner_len:
            raise ValueError(f"Inconsistent inner tuple length at index {i}.")


def _add_two_tuples(tuple_a: Tuple[int, ...], tuple_b: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    Performs element-wise addition of two tuples of integers.
    """
    if len(tuple_a) != len(tuple_b):
        raise ValueError("Tuples must have the same length for element-wise addition.")

    result_list = []
    for i in range(len(tuple_a)):
        val_a = tuple_a[i]
        val_b = tuple_b[i]

        if not isinstance(val_a, (int, float)) or not isinstance(val_b, (int, float)):
            raise TypeError("All elements within nested tuples must be numbers.")

        sum_val = val_a + val_b
        result_list.append(sum_val)

    return tuple(result_list)


def add_nested_tuples(nested_tuple_1: Tuple[Tuple[int, ...], ...], 
                       nested_tuple_2: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    """
    Performs index-wise addition of elements in two nested tuples.

    Example:
    Input:  ((1, 3), (4, 5))
    Input:  ((6, 7), (3, 9))
    Output: ((7, 10), (7, 14))
    """
    # Step 1: Validate structural integrity of inputs
    _validate_nested_tuple_structure(nested_tuple_1)
    _validate_nested_tuple_structure(nested_tuple_2)

    # Handle empty input case
    if len(nested_tuple_1) == 0:
        return ()

    # Step 2: Check that the outer tuples have the same number of inner tuples
    len1 = len(nested_tuple_1)
    len2 = len(nested_tuple_2)

    if len1 != len2:
        raise ValueError("The two nested tuples must have the same number of inner tuples.")

    # Step 3: Perform the addition
    final_result = []

    for i in range(len1):
        inner_a = nested_tuple_1[i]
        inner_b = nested_tuple_2[i]

        # Add the inner tuples element-wise
        sum_inner = _add_two_tuples(inner_a, inner_b)
        final_result.append(sum_inner)

    # Step 4: Convert the result list to a tuple to maintain type consistency
    return tuple(final_result)

if __name__ == "__main__":
    # Assertions provided in the requirements
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))