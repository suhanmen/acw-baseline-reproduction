def pancake_sort(arr):
    """
    Sorts a list of elements using the pancake sort algorithm.
    The pancake sort algorithm works by repeatedly finding the maximum 
    element of the unsorted portion and moving it to the end by flipping 
    the prefix of the list twice.
    """
    n = len(arr)
    # Work from the end of the list to the beginning
    for curr_size in range(n, 1, -1):
        # Find the index of the maximum element in arr[0...curr_size-1]
        max_idx = 0
        for i in range(1, curr_size):
            if arr[i] > arr[max_idx]:
                max_idx = i

        # If the max element is not already at its correct position
        if max_idx != curr_size - 1:
            # 1. Flip the prefix to move the max element to the front
            if max_idx != 0:
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]

            # 2. Flip the prefix to move the max element to its correct position
            arr[:curr_size] = arr[:curr_size][::-1]

    return arr

if __name__ == "__main__":
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]