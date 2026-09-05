import heapq

def merge_sorted_list(*lists):
    heap = []
    # Initialize the heap with the first element of each list
    for lst in lists:
        if lst:
            heapq.heappush(heap, (lst[0], lst, 0))

    merged = []
    while heap:
        current_val, current_list, current_index = heapq.heappop(heap)
        merged.append(current_val)
        # Push the next element from the current list into the heap
        if current_index + 1 < len(current_list):
            next_index = current_index + 1
            heapq.heappush(heap, (current_list[next_index], current_list, next_index))

    return merged