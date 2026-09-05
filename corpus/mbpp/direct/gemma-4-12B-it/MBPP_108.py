import heapq

def merge_sorted_list(*lists):
    """
    Merge multiple sorted inputs into a single sorted list using a heap queue.
    Note: The input lists provided in the problem description are not pre-sorted 
    (e.g., [25, 24, 15...]). However, the logic of "merge sorted inputs" 
    traditionally implies the inputs are sorted. Given the assertions, the 
    inputs provided are unsorted, so we must sort the individual lists 
    first to satisfy the "merge" logic, or treat the final result as the 
    sorted combination of all elements. 

    To strictly follow the Heap Queue Algorithm for merging sorted streams:
    1. Sort individual lists first (as they are unsorted in the test cases).
    2. Use a min-heap to yield the smallest current element from all lists.
    """
    # The test cases provided have unsorted input lists but expect a fully sorted output.
    # To use a heap merge algorithm correctly, inputs must be sorted.
    sorted_lists = [sorted(lst) for lst in lists]

    heap = []
    # Initialize heap with the first element of each non-empty list
    # Store as (value, list_index, element_index)
    for i, lst in enumerate(sorted_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        # If there is a next element in the same list, push it to heap
        if element_idx + 1 < len(sorted_lists[list_idx]):
            next_val = sorted_lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return result

if __name__ == "__main__":
    assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
    assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]