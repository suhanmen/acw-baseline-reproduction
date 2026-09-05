import heapq
from typing import List, Any

def heap_assending(input_list: List[Any]) -> List[Any]:
    """
    Sorts a given list of elements in ascending order using the heap queue algorithm.

    This function implements the Heapsort algorithm, which has a time complexity of O(n log n).
    It explicitly handles edge cases such as empty lists, single-element lists, 
    lists with all equal elements, and lists containing negative or zero values.

    Args:
        input_list (List[Any]): The list of elements to be sorted.

    Returns:
        List[Any]: A new list containing the sorted elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-comparable elements.
    """

    # Step 1: Validate that the input is a list
    if not isinstance(input_list, list):
        raise TypeError(
            f"Expected input to be of type 'list', but received type '{type(input_list).__name__}'."
        )

    # Step 2: Handle the edge case where the input list is empty
    if len(input_list) == 0:
        return []

    # Step 3: Handle the edge case where the input list contains a single element
    if len(input_list) == 1:
        # Create a copy to avoid mutating the original list, though for single element it's trivial
        return input_list.copy()

    # Step 4: Create a copy of the input list to ensure the original list is not modified.
    # This is a standard practice in functional-style or defensive programming.
    sorted_list_copy = input_list.copy()

    # Step 5: Attempt to validate comparability of elements by trying to compare the first two.
    # This helps catch TypeError before running the full sort.
    if len(sorted_list_copy) >= 2:
        try:
            # Check if elements are comparable by attempting a simple comparison
            _ = sorted_list_copy[0] < sorted_list_copy[1]
        except TypeError as type_error:
            raise ValueError(
                "All elements in the list must be comparable. "
                f"Error occurred while comparing types: {type_error}"
            )

    # Step 6: Transform the list into a heap in O(n) time.
    # heapq.heapify transforms the list in-place into a heap, satisfying the heap invariant.
    # Since we want ascending order, we use a min-heap.
    heapq.heapify(sorted_list_copy)

    # Step 7: Extract elements one by one from the heap to build the sorted list.
    # We will construct a new list to ensure we don't return the heap object directly.
    final_sorted_list = []

    # Loop continues until the heap is empty
    while len(sorted_list_copy) > 0:
        # heappop extracts the smallest element from the heap and returns it.
        # This operation is O(log n).
        smallest_element = heapq.heappop(sorted_list_copy)
        final_sorted_list.append(smallest_element)

    # Step 8: Return the newly constructed sorted list.
    return final_sorted_list