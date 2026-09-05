from typing import Tuple, List, Any

def zip_tuples(tuple1: Tuple[Any, ...], tuple2: Tuple[Any, ...]) -> List[Tuple[Any, ...]]:
    """
    Zips two tuples together by cycling the second tuple repeatedly until
    the first tuple is fully exhausted.

    Args:
        tuple1: The primary tuple whose length determines the length of the output.
        tuple2: The secondary tuple whose elements are cycled to match the length of tuple1.

    Returns:
        A list of tuples where each element is a pair from the two inputs.

    Raises:
        TypeError: If inputs are not tuples.
        ValueError: If the second tuple is empty but the first tuple is not.
    """
    # Validate input types
    if not isinstance(tuple1, tuple):
        raise TypeError(f"First argument must be a tuple, got {type(tuple1).__name__}")
    if not isinstance(tuple2, tuple):
        raise TypeError(f"Second argument must be a tuple, got {type(tuple2).__name__}")

    # Handle edge case: Empty first tuple
    # If the first tuple is empty, the result is an empty list regardless of the second tuple.
    if len(tuple1) == 0:
        return []

    # Handle edge case: Empty second tuple when first tuple is not empty
    # This would result in an infinite loop or an error if we tried to access index 0.
    if len(tuple2) == 0:
        raise ValueError("The second tuple cannot be empty if the first tuple contains elements.")

    result: List[Tuple[Any, ...]] = []

    # We need to iterate through every index of the first tuple.
    # Since the second tuple repeats, we use the modulo operator on the index.
    num_elements_in_first = len(tuple1)
    num_elements_in_second = len(tuple2)

    for i in range(num_elements_in_first):
        # Retrieve the element from the first tuple
        val1 = tuple1[i]

        # Calculate the index for the second tuple using modulo
        # This ensures that once we reach the end of tuple2, we wrap back to 0.
        secondary_index = i % num_elements_in_second
        val2 = tuple2[secondary_index]

        # Construct the pair
        pair = (val1, val2)

        # Append to the result list
        result.append(pair)

    return result

# The following assertions check the behavior against the provided requirements.
if __name__ == "__main__":
    # Test Case 1
    assert zip_tuples((7, 8, 4, 5, 9, 10), (1, 5, 6)) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]

    # Test Case 2
    assert zip_tuples((8, 9, 5, 6, 10, 11), (2, 6, 7)) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]

    # Test Case 3
    assert zip_tuples((9, 10, 6, 7, 11, 12), (3, 7, 8)) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]