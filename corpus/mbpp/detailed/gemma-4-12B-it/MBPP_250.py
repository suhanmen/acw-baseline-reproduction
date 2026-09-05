from typing import Tuple, Any, Union

def count_X(data_tuple: Tuple[Any, ...], target_element: Any) -> int:
    """
    Counts the number of occurrences of a specific element within a tuple.

    Args:
        data_tuple (Tuple): A tuple containing elements of any type.
        target_element (Any): The value to count within the tuple.

    Returns:
        int: The total count of target_element in data_tuple.

    Raises:
        TypeError: If the provided data_tuple is not a tuple.
        ValueError: If the data_tuple is None.
    """
    # Validate that data_tuple is not None
    if data_tuple is None:
        raise ValueError("The input data_tuple cannot be None.")

    # Validate that data_tuple is actually a tuple type
    if not isinstance(data_tuple, tuple):
        raise TypeError(f"Expected a tuple for the first argument, but got {type(data_tuple).__name__}")

    # Initialize a counter variable
    occurrence_count: int = 0

    # Handle the case of an empty tuple explicitly
    # The loop will naturally handle this, but it's good to acknowledge as an edge case
    if len(data_tuple) == 0:
        return occurrence_count

    # Iterate through each item in the tuple
    for current_item in data_tuple:
        # Perform a comparison to see if the item matches the target
        # Using '==' handles types that support equality comparison
        if current_item == target_element:
            # Increment count if a match is found
            occurrence_count += 1

    # Return the final accumulated count
    return occurrence_count

# Test assertions provided in the problem description
if __name__ == "__main__":
    # Case 1: Element not present
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0

    # Case 2: Element present (10 appears 3 times)
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 3

    # Case 3: Element present (8 appears 4 times)
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8) == 4

    # Additional edge cases for production-grade robustness
    # Empty tuple
    assert count_X((), 10) == 0
    # Single element match
    assert count_X((5,), 5) == 1
    # Single element mismatch
    assert count_X((5,), 10) == 0
    # All elements are the target
    assert count_X((1, 1, 1), 1) == 3
    # Mixed types
    assert count_X((1, "1", 1.0), 1) == 2  # 1 and 1.0 are equal in Python