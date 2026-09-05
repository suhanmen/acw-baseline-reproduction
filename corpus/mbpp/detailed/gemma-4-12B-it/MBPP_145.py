from typing import Iterable, Union

def max_Abs_Diff(elements: Iterable[Union[int, float]], length: int) -> float:
    """
    Calculates the maximum absolute difference between any two elements 
    in a given collection.

    The maximum absolute difference in a set of numbers is always the 
    difference between the maximum value and the minimum value.

    Args:
        elements: An iterable of integers or floats.
        length: The expected length of the input collection.

    Returns:
        The maximum absolute difference as a float or int.

    Raises:
        ValueError: If the input is empty or has only one element.
        TypeError: If elements are not numbers or if length is incorrect.
    """

    # Step 1: Validate the length parameter
    # Even though we can determine length from the iterable, the signature 
    # provides a length, so we should verify consistency if possible.
    # However, since the input is an Iterable, we convert it to a list first.
    data_list = list(elements)
    actual_length = len(data_list)

    if actual_length != length:
        # We handle this to ensure the function adheres strictly to the 
        # provided length metadata.
        raise ValueError(f"Expected length {length}, but received {actual_length}.")

    # Step 2: Handle edge cases for collection size
    if actual_length == 0:
        raise ValueError("Input collection is empty; cannot calculate difference.")

    if actual_length == 1:
        # Difference between an element and itself is 0
        return 0.0

    # Step 3: Validate that all elements are numeric
    for item in data_list:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric. Found: {type(item).__name__}")

    # Step 4: Identify the extremes
    # The maximum difference is mathematically defined as max(S) - min(S).
    # This avoids O(n^2) comparisons by using O(n) scans.

    try:
        min_value = min(data_list)
        max_value = max(data_list)
    except ValueError:
        # This should be unreachable given the checks above, but kept for robustness
        raise ValueError("Failed to determine min/max of the collection.")

    # Step 5: Calculate the absolute difference
    # Since max_value is >= min_value, (max_value - min_value) is always non-negative.
    difference = max_value - min_value

    # Ensure we return the absolute value (redundant but defensive)
    abs_difference = abs(difference)

    return abs_difference

if __name__ == "__main__":
    # Assertions provided in the prompt
    assert max_Abs_Diff((2, 1, 5, 3), 4) == 4
    assert max_Abs_Diff((9, 3, 2, 5, 1), 5) == 8
    assert max_Abs_Diff((3, 2, 1), 3) == 2