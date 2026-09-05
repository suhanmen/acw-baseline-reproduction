from typing import Tuple, List

def extract_min_max(data: Tuple[int, ...], k: int) -> Tuple[int, ...]:
    """
    Extracts the k smallest and k largest elements from a tuple of integers.
    The final result is returned as a sorted tuple of all included elements.

    Note: If k is larger than the number of unique elements, or if the 
    total elements required exceed the length of the tuple, 
    this implementation handles logic to avoid index errors and ensures 
    validity.

    Args:
        data: A tuple of integers.
        k: The number of minimum and maximum elements to extract.

    Returns:
        A tuple containing the k minimums and k maximums, sorted in ascending order.
    """
    # Validate input types
    if not isinstance(data, tuple):
        raise TypeError("Input 'data' must be a tuple.")
    if not isinstance(k, int):
        raise TypeError("Input 'k' must be an integer.")
    if k < 0:
        raise ValueError("Input 'k' must be a non-negative integer.")

    # Handle empty input case
    if not data:
        return ()

    # If k is 0, the result is an empty tuple
    if k == 0:
        return ()

    # Create a list from the tuple to allow for processing
    # We use a list to handle duplicates correctly as per the logic of "extracting"
    input_list = list(data)
    input_length = len(input_list)

    # If k is larger than half the length of the data, the logic 
    # of "k smallest and k largest" might overlap entirely or exceed data size.
    # Based on the provided assertions, we need to identify k smallest and k largest.
    # If there aren't enough elements to pick k distinct positions for min and max
    # without overlap, we must be careful.
    # However, the assertions show that if k is 3 and length is 6, 
    # we get all 6. If k is 4 and length is 7, we get all 7.

    # Let's follow the standard interpretation: 
    # Identify the k smallest values and the k largest values.
    # If the sets overlap (e.g., k=4, length=7), we need to ensure we 
    # don't double-count specific indices but include all values that fall
    # into either the "k smallest" or "k largest" category.

    # Step 1: Sort the data to easily identify bounds
    sorted_data = sorted(input_list)

    # Step 2: Identify the indices for the k smallest
    # These are the first k elements in the sorted list
    # If k > length, it takes all elements
    min_count = min(k, input_length)
    min_elements = sorted_data[:min_count]

    # Step 3: Identify the indices for the k largest
    # These are the last k elements in the sorted list
    max_count = min(k, input_length)
    max_elements = sorted_data[input_length - max_count:]

    # Step 4: Combine the results
    # We combine the lists and use a set of indices to ensure that if 
    # an element is both one of the k smallest and one of the k largest,
    # we don't duplicate its position in the final count if the problem 
    # implies "unique indices".
    # Looking at the assertions:
    # (5, 20, 3, 7, 6, 8), k=2 -> min(3, 5), max(8, 20) -> (3, 5, 8, 20)
    # (4, 5, 6, 1, 2, 7), k=3 -> min(1, 2, 4), max(5, 6, 7) -> (1, 2, 4, 5, 6, 7)
    # (2, 3, 4, 8, 9, 11, 7), k=4 -> min(2, 3, 4, 7), max(8, 9, 11, 7) -> (2, 3, 4, 7, 8, 9, 11)

    # The assertions suggest we take the first k indices and the last k indices 
    # of the sorted list and merge them into a unique set of values.
    # Wait, let's re-examine assertion 3: 
    # Input: (2, 3, 4, 8, 9, 11, 7), k=4. Sorted: (2, 3, 4, 7, 8, 9, 11)
    # k smallest: (2, 3, 4, 7). k largest: (8, 9, 11, 7).
    # Union: (2, 3, 4, 7, 8, 9, 11). 
    # This confirms we are taking the union of the first k and last k elements of the sorted list.

    # To handle duplicates correctly (if the same value appears multiple times),
    # we should work with indices.

    result_indices = set()

    # Add indices of k smallest
    for i in range(min_count):
        result_indices.add(i)

    # Add indices of k largest
    # The indices for the last k elements are from (length - max_count) to (length - 1)
    start_max_idx = input_length - max_count
    for i in range(start_max_idx, input_length):
        result_indices.add(i)

    # Extract the values using the unique indices
    # We must sort the indices to maintain the relative order of the sorted_data
    sorted_indices = sorted(list(result_indices))
    final_list = []
    for idx in sorted_indices:
        final_list.append(sorted_data[idx])

    return tuple(final_list)