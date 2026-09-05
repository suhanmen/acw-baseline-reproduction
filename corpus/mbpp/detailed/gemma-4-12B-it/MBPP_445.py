from typing import Tuple, Any

def index_multiplication(tuple1: Tuple[Tuple[Any, ...], ...], 
                         tuple2: Tuple[Tuple[Any, ...], ...]) -> Tuple[Tuple[Any, ...], ...]:
    """
    Performs index-wise multiplication of nested tuples.

    For example, if tuple1 is ((a1, a2), (a3, a4)) and tuple2 is ((b1, b2), (b3, b4)),
    the result will be ((a1*b1, a2*b2), (a3*b3, a4*b4)).

    Args:
        tuple1: A tuple of tuples containing numeric values.
        tuple2: A tuple of tuples containing numeric values.

    Returns:
        A tuple of tuples containing the results of the multiplication.

    Raises:
        ValueError: If the input tuples are not of the same length or if 
                    the nested tuples within them do not have matching lengths.
        TypeError: If inputs are not tuples or contain non-numeric types.
    """

    # 1. Validate basic input types
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise TypeError("Both inputs must be tuples.")

    # 2. Check if the outer tuples have the same length
    len1 = len(tuple1)
    len2 = len(tuple2)

    if len1 != len2:
        raise ValueError(f"Outer tuples must have the same length. "
                         f"Got {len1} and {len2}.")

    # Handle the edge case of empty outer tuples
    if len1 == 0:
        return ()

    result_list = []

    # 3. Iterate through the outer tuples by index
    for i in range(len1):
        inner_tuple1 = tuple1[i]
        inner_tuple2 = tuple2[i]

        # Validate nested types
        if not isinstance(inner_tuple1, tuple) or not isinstance(inner_tuple2, tuple):
            raise TypeError(f"Elements at index {i} must be tuples.")

        # Validate inner tuple lengths
        inner_len1 = len(inner_tuple1)
        inner_len2 = len(inner_tuple2)

        if inner_len1 != inner_len2:
            raise ValueError(f"Nested tuples at index {i} must have the same length. "
                             f"Got {inner_len1} and {inner_len2}.")

        # Handle empty inner tuples
        if inner_len1 == 0:
            result_list.append(())
            continue

        # 4. Perform index-wise multiplication on the inner tuples
        multiplied_inner_elements = []
        for j in range(inner_len1):
            val1 = inner_tuple1[j]
            val2 = inner_tuple2[j]

            # Check if values are numeric
            if not (isinstance(val1, (int, float)) and isinstance(val2, (int, float))):
                raise TypeError(f"Non-numeric values found at index ({i}, {j}).")

            product = val1 * val2
            multiplied_inner_elements.append(product)

        # Convert the list of products back into a tuple
        result_list.append(tuple(multiplied_inner_elements))

    # 5. Convert the final list of tuples into a nested tuple
    final_result = tuple(result_list)
    return final_result