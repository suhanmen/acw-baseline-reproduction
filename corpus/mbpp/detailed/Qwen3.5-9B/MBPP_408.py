from typing import List, Tuple, Optional
import heapq

def _validate_inputs(
    array_a: List[int],
    array_b: List[int],
    k: int
) -> Tuple[bool, Optional[str]]:
    """
    Validates the inputs for the k_smallest_pairs function.

    Returns:
        A tuple (is_valid, error_message).
        - If valid: (True, None)
        - If invalid: (False, "description of error")
    """
    # Check if k is non-negative
    if not isinstance(k, int) or k < 0:
        return False, "k must be a non-negative integer."

    # Check if k is excessively large to avoid unnecessary computation
    # The maximum number of pairs possible is len(array_a) * len(array_b)
    max_possible_pairs = len(array_a) * len(array_b)
    if k > max_possible_pairs:
        return False, f"k cannot exceed the total number of pairs ({max_possible_pairs})."

    # Check if array_a contains only integers
    if not isinstance(array_a, list):
        return False, "The first array must be a list."
    if not all(isinstance(item, int) for item in array_a):
        return False, "The first array must contain only integers."

    # Check if array_b contains only integers
    if not isinstance(array_b, list):
        return False, "The second array must be a list."
    if not all(isinstance(item, int) for item in array_b):
        return False, "The second array must contain only integers."

    return True, None

def _generate_single_pairs(
    array_a: List[int],
    array_b: List[int],
    i: int,
    j: int
) -> Tuple[int, int, int]:
    """
    Generates a single pair and calculates its sum.

    Returns:
        A tuple (sum_value, element_a, element_b)
    """
    sum_value = array_a[i] + array_b[j]
    return sum_value, array_a[i], array_b[j]

def _extract_pair_items(sum_value: int, element_a: int, element_b: int) -> List[int]:
    """
    Extracts the pair from the internal representation.

    Returns:
        A list [element_a, element_b]
    """
    return [element_a, element_b]

def k_smallest_pairs(
    array_a: List[int],
    array_b: List[int],
    k: int
) -> List[List[int]]:
    """
    Finds the k smallest pairs, where each pair consists of one element from 
    the first array and one element from the second array. Pairs are compared 
    based on the sum of their elements.

    Args:
        array_a: The first list of integers.
        array_b: The second list of integers.
        k: The number of pairs to return.

    Returns:
        A list of k pairs (each pair is a list of two integers) with the smallest sums.
        If k is 0, an empty list is returned.
        If k is larger than the total number of possible pairs, all possible pairs are returned.
    """
    # Step 1: Validate inputs
    is_valid, error_message = _validate_inputs(array_a, array_b, k)

    if not is_valid:
        raise ValueError(error_message)

    # Step 2: Handle the edge case where k is 0
    if k == 0:
        return []

    # Step 3: Handle edge cases where one or both arrays are empty
    # If either array is empty, no pairs can be formed.
    if len(array_a) == 0 or len(array_b) == 0:
        return []

    # Step 4: Determine the actual number of pairs to generate
    # We cannot return more pairs than exist.
    total_possible_pairs = len(array_a) * len(array_b)
    effective_k = min(k, total_possible_pairs)

    # Step 5: Handle the edge case where total possible pairs is less than the original k
    # (Handled by effective_k, but we need to ensure we don't process more than necessary)

    # Step 6: Use a min-heap to find the k smallest pairs efficiently.
    # The heap will store tuples: (sum_value, index_in_array_a, index_in_array_b)
    # We only initialize the heap with the first element of each row in the conceptual
    # matrix of all pairs (array_a[i] + array_b[0]). This avoids creating the full cartesian product upfront.

    min_heap: List[Tuple[int, int, int]] = []

    # Step 7: Populate the initial heap
    # We iterate through the first array and pair each element with the first element of the second array.
    for i in range(len(array_a)):
        # Calculate the sum of the pair (array_a[i], array_b[0])
        current_sum = array_a[i] + array_b[0]
        # Push the tuple (sum, index_a, index_b) into the heap
        heapq.heappush(min_heap, (current_sum, i, 0))

    result_pairs: List[List[int]] = []

    # Step 8: Extract the smallest pair k times (or until the heap is empty)
    while effective_k > 0 and len(min_heap) > 0:
        # Pop the smallest element from the heap
        _, index_a, index_b = heapq.heappop(min_heap)

        # Validate the popped indices (defensive coding, though logic guarantees validity)
        if index_a < 0 or index_a >= len(array_a) or index_b < 0 or index_b >= len(array_b):
            break

        # Create the pair list
        pair = [array_a[index_a], array_b[index_b]]
        result_pairs.append(pair)

        # Decrement the count of pairs we still need to find
        effective_k -= 1

        # Step 9: If there are more elements in array_b to pair with array_a[index_a],
        # add the next potential candidate to the heap.
        # The next candidate for this specific row (index_a) would be index_b + 1.
        next_index_b = index_b + 1

        if next_index_b < len(array_b):
            new_sum = array_a[index_a] + array_b[next_index_b]
            heapq.heappush(min_heap, (new_sum, index_a, next_index_b))

    # Step 10: Return the collected pairs
    return result_pairs