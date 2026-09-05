def _validate_and_normalize_tuple(element, path):
    """
    Recursively validates that the structure consists solely of tuples of numbers (int or float).
    Also normalizes the input by ensuring uniform types (converts all to a common numeric type if needed).
    Returns a new normalized structure or raises a ValueError on invalid structure.

    Args:
        element: The current element being validated (should be tuple or number).
        path: A string representing the current path in the structure for error messages.

    Returns:
        The normalized tuple or number.

    Raises:
        ValueError: If the structure or content is invalid.
    """
    if isinstance(element, tuple):
        if not element:
            raise ValueError(f"Empty tuple found at path '{path}'")

        normalized_elements = []
        for index, item in enumerate(element):
            new_path = f"{path}[{index}]"
            normalized_item = _validate_and_normalize_tuple(item, new_path)
            normalized_elements.append(normalized_item)

        return tuple(normalized_elements)

    # If it's not a tuple, it should be a number
    if isinstance(element, (int, float)):
        return element

    raise ValueError(f"Invalid data type at path '{path}'. Expected tuple or number, got {type(element).__name__}")


def _deep_add_sequences(seq1, seq2, path_prefix):
    """
    Helper function to perform element-wise addition of two sequences (tuples) recursively.

    Args:
        seq1: First sequence of numbers (nested tuples).
        seq2: Second sequence of numbers (nested tuples).
        path_prefix: String for debugging/error reporting.

    Returns:
        A new tuple containing the sums.
    """
    # Check lengths match
    len1 = len(seq1)
    len2 = len(seq2)

    if len1 != len2:
        raise ValueError(
            f"Mismatched tuple lengths at path '{path_prefix}'."
            f"First has {len1} elements, second has {len2} elements."
        )

    result = []
    for i in range(len1):
        current_path = f"{path_prefix}[{i}]"
        val1 = seq1[i]
        val2 = seq2[i]

        if isinstance(val1, tuple) and isinstance(val2, tuple):
            # Recurse
            summed_nested = _deep_add_sequences(val1, val2, current_path)
            result.append(summed_nested)
        else:
            # Add numbers
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise ValueError(f"Non-numeric values found at path '{current_path}'")

            s = val1 + val2
            result.append(s)

    return tuple(result)


def add_nested_tuples(tuple1, tuple2):
    """
    Performs index-wise addition of elements in two nested tuples.

    Both input tuples must:
    1. Have the same length.
    2. Contain only integers or floats.
    3. At each index where one element is a tuple, the corresponding element in the other
       must also be a tuple.
    4. Nested tuples at corresponding indices must themselves have matching structures and lengths.

    Returns:
        A new nested tuple with added values.

    Raises:
        ValueError: If inputs do not meet the structural requirements.
        TypeError: If inputs are not tuples.
    """
    # 1. Validate top-level type
    if not isinstance(tuple1, tuple):
        raise TypeError(f"First argument must be a tuple, got {type(tuple1).__name__}")
    if not isinstance(tuple2, tuple):
        raise TypeError(f"Second argument must be a tuple, got {type(tuple2).__name__}")

    # 2. Validate structure and normalize
    # We create deep copies with validation to ensure safety and type consistency
    try:
        normalized_tuple1 = _validate_and_normalize_tuple(tuple1, "root[0]")
        normalized_tuple2 = _validate_and_normalize_tuple(tuple2, "root[1]")
    except ValueError as e:
        raise ValueError(f"Validation failed: {str(e)}") from e

    # 3. Perform the addition
    try:
        result = _deep_add_sequences(normalized_tuple1, normalized_tuple2, "root")
    except ValueError as e:
        raise ValueError(f"Addition logic failed: {str(e)}") from e

    return result