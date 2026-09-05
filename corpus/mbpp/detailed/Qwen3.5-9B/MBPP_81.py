from typing import Tuple, Any, List

def zip_tuples(tuple_a: Tuple[Any, ...], tuple_b: Tuple[Any, ...]) -> List[Tuple[Any, ...]]:
    """
    Zips two given tuples element-wise by repeating the shorter tuple as needed.

    This function follows these rules:
    1. It takes two tuples as input.
    2. It creates pairs by taking one element from each tuple in sequence.
    3. If one tuple is longer than the other, the shorter tuple is cycled through 
       repeatedly to match the length of the longer tuple.
    4. The result is a list of tuples, where each inner tuple contains one element 
       from the first tuple and one from the second.

    Args:
        tuple_a: The first input tuple.
        tuple_b: The second input tuple.

    Returns:
        A list of tuples, where each tuple contains corresponding elements from 
        the input tuples (with the shorter one cycled).

    Raises:
        TypeError: If either input is not a tuple.

    Examples:
        >>> zip_tuples((7, 8, 4, 5, 9, 10), (1, 5, 6))
        [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
        >>> zip_tuples((8, 9, 5, 6, 10, 11), (2, 6, 7))
        [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
    """

    # Step 1: Validate that both inputs are tuples.
    if not isinstance(tuple_a, tuple):
        raise TypeError(f"First argument must be a tuple, got {type(tuple_a).__name__}")

    if not isinstance(tuple_b, tuple):
        raise TypeError(f"Second argument must be a tuple, got {type(tuple_b).__name__}")

    # Step 2: Get the lengths of both tuples.
    length_a: int = len(tuple_a)
    length_b: int = len(tuple_b)

    # Step 3: Handle the case where both tuples are empty.
    if length_a == 0 and length_b == 0:
        return []

    # Step 4: Determine the maximum length needed for the output.
    max_length: int = max(length_a, length_b)

    # Step 5: Initialize an empty list to store the result.
    result: List[Tuple[Any, ...]] = []

    # Step 6: Loop through the indices from 0 up to (but not including) max_length.
    current_index_a: int = 0
    current_index_b: int = 0

    for i in range(max_length):
        # Step 7: Get the current index for the first tuple.
        # If the index exceeds the tuple's length, wrap around to 0.
        index_a: int = current_index_a % length_a if length_a > 0 else 0

        # Step 8: Get the current index for the second tuple.
        # If the index exceeds the tuple's length, wrap around to 0.
        index_b: int = current_index_b % length_b if length_b > 0 else 0

        # Step 9: Increment the counters for the next iteration.
        current_index_a += 1
        current_index_b += 1

        # Step 10: Retrieve the elements at the calculated indices.
        element_a: Any = tuple_a[index_a]
        element_b: Any = tuple_b[index_b]

        # Step 11: Create a new tuple containing the two elements.
        current_pair: Tuple[Any, ...] = (element_a, element_b)

        # Step 12: Append the current pair to the result list.
        result.append(current_pair)

    # Step 13: Return the final list of tuples.
    return result