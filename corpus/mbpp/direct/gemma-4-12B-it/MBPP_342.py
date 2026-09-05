import heapq

def find_minimum_range(nums: list[list[int]]) -> tuple[int, int]:
    """
    Finds the smallest range that includes at least one element from each of the 
    given sorted arrays.
    """
    # min_heap stores tuples of (value, array_index, element_index)
    min_heap = []
    current_max = float('-inf')

    # Initialize the heap with the first element of each list
    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i][0], i, 0))
        current_max = max(current_max, nums[i][0])

    # Initialize the result with a large range
    res_start, res_end = float('-inf'), float('inf')

    while min_heap:
        current_min, list_idx, element_idx = heapq.heappop(min_heap)

        # Update the best range if the current range is smaller
        if current_max - current_min < res_end - res_start:
            res_start, res_end = current_min, current_max

        # If we have reached the end of one of the lists, we cannot shrink
        # the range further while still including an element from every list.
        if element_idx + 1 == len(nums[list_idx]):
            break

        # Push the next element from the same list into the heap
        next_val = nums[list_idx][element_idx + 1]
        heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

        # Update current_max as we add new elements
        current_max = max(current_max, next_val)

    return (res_start, res_end)