import heapq

def merge_sorted_list(*sorted_lists):
    # First, validate that all inputs are lists and not empty
    if any(not isinstance(lst, list) or len(lst) == 0 for lst in sorted_lists):
        raise ValueError("All inputs must be non-empty lists")

    # Function to yield the smallest element and update the heap
    def heapify_and_merge(*lists):
        heap = []
        # Push the first element of each list into the heap along with the list index and element index
        for i, lst in enumerate(lists):
            if lst:  # Check if the list is not empty
                first_element = lst[0]
                heapq.heappush(heap, (first_element, i, 0))

        while heap:
            current_min, list_index, element_index = heapq.heappop(heap)
            yield current_min

            # If there are more elements in the same list, push the next element into the heap
            if element_index + 1 < len(sorted_lists[list_index]):
                next_element = sorted_lists[list_index][element_index + 1]
                heapq.heappush(heap, (next_element, list_index, element_index + 1))

    # Generate the merged sorted iterator
    merged = heapify_and_merge(*sorted_lists)

    # Convert the iterator to a list to return the result
    return list(merged)