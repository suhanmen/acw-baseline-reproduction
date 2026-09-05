def median_numbers(a: float, b: float, c: float) -> float:
    """
    Computes the median value of three specific numeric inputs.

    The median is defined as the value that appears in the middle when the three
    values are sorted in non-decreasing order.

    This implementation:
    1. Validates that exactly three numeric arguments are provided (handled by signature).
    2. Handles cases where values are equal (including all three being equal).
    3. Handles negative numbers, zero, and large numbers.
    4. Returns a float result to ensure consistency with the expected assertions.

    Args:
        a (float): First number.
        b (float): Second number.
        c (float): Third number.

    Returns:
        float: The median of the three numbers.

    Raises:
        TypeError: If any argument is not a number (int or float).
    """

    # Step 1: Validate input types explicitly.
    # We check if 'a', 'b', and 'c' are instances of int or float.
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, got {type(b).__name__}")
    if not isinstance(c, (int, float)):
        raise TypeError(f"Third argument must be a number, got {type(c).__name__}")

    # Step 2: Create a list of the three numbers to facilitate sorting.
    # This abstracts the values into a mutable sequence.
    numbers_list = [a, b, c]

    # Step 3: Sort the list in ascending order.
    # The sort is stable and handles negative/zero/positive uniformly.
    sorted_numbers = sorted(numbers_list)

    # Step 4: Identify the middle element (the median).
    # For a list of length 3, the median is always at index 1.
    median_value = sorted_numbers[1]

    # Step 5: Ensure the return type is a float to match the assertion expectations
    # (e.g., asserting == 55.0). While Python handles int comparison with float well,
    # explicitly returning a float guarantees type consistency for strict checkers.
    if isinstance(median_value, int):
        median_float = float(median_value)
    else:
        median_float = median_value

    return median_float