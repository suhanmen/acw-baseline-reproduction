from typing import List, Union

Number = Union[int, float]

def frequency_Of_Largest(n: int, arr: List[Number]) -> int:
    """
    Find the frequency of the largest value in a given array.

    Args:
        n (int): The expected number of elements in the array.
                 This parameter is validated against the actual length of arr.
        arr (List[Number]): A list of numbers.

    Returns:
        int: The frequency of the largest number in the list.

    Raises:
        ValueError: If n is negative.
        ValueError: If the length of arr is not equal to n.
        ValueError: If arr contains non-numeric elements.
        ValueError: If arr is None.
    """

    # Validation: Check if n is non-negative
    if n < 0:
        raise ValueError(f"Parameter 'n' must be non-negative, got {n}")

    # Validation: Check if arr is None
    if arr is None:
        raise ValueError("Parameter 'arr' cannot be None")

    # Validation: Check if the actual length matches n
    actual_length = len(arr)
    if actual_length != n:
        raise ValueError(f"Length of array ({actual_length}) does not match parameter 'n' ({n})")

    # Validation: Check if the array contains only valid numeric types
    for index, value in enumerate(arr):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid element type at index {index}: expected number, got {type(value).__name__}")

        # Explicit check for booleans since bool is a subclass of int in Python
        # and we typically want to treat booleans as separate or handle them explicitly.
        # However, the problem implies numeric arrays. If strict numeric is needed:
        if isinstance(value, bool):
            raise ValueError(f"Invalid element type at index {index}: booleans are not allowed")

    # Edge Case: Empty array
    # Although the assertion implies n >= 1 based on the examples (5, 3, 4 elements),
    # we handle the case where n could theoretically be 0 if passed.
    if n == 0:
        return 0

    # Step 1: Identify the maximum value in the array
    # We use the built-in max function for clarity and reliability.
    # We have already validated that the array is not empty (n > 0).
    max_value = max(arr)

    # Step 2: Calculate the frequency of this maximum value
    count = 0

    # We iterate explicitly to demonstrate the logic step-by-step,
    # rather than using a one-liner with sum and generator expressions.
    for element in arr:
        if element == max_value:
            count += 1

    return count