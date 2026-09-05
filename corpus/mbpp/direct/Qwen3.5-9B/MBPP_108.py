import heapq

def merge_sorted_list(*lists):
    iterator = iter(lists)
    heap = []
    for i, lst in enumerate(iterator):
        lst_iter = iter(lst)
        try:
            val = next(lst_iter)
            heapq.heappush(heap, (val, i, lst_iter))
        except StopIteration:
            continue

    result = []
    while heap:
        val, idx, it = heapq.heappop(heap)
        result.append(val)
        try:
            next_val = next(it)
            heapq.heappush(heap, (next_val, idx, it))
        except StopIteration:
            continue
    return result