import heapq

def heap_assending(arr):
    """
    Sorts a given list of elements in ascending order using the heap queue algorithm.

    Args:
        arr (list): A list of comparable elements.

    Returns:
        list: A new list containing the elements sorted in ascending order.
    """
    # Create a copy of the list to avoid modifying the original input
    heap = list(arr)

    # Transform the list into a min-heap in-place
    heapq.heapify(heap)

    # Pop elements from the heap one by one to build the sorted list
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))

    return sorted_list

if __name__ == "__main__":
    assert heap_assending([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]) == [1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 18]
    assert heap_assending([25, 35, 22, 85, 14, 65, 75, 25, 58]) == [14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_assending([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]