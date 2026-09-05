def get_Position(arr, n, k):
    # Simulate removing elements one by one from the array until k elements are removed
    # We return the position (0-based index) of the last removed element
    index = 0
    for _ in range(k):
        # Current element at index to be removed
        removed_element = arr[index]
        # Shift all subsequent elements to the left
        for i in range(index + 1, len(arr) - 1):
            arr[i] = arr[i + 1]
        # Remove the last element which is now a duplicate of the shifted one
        del arr[-1]
        # If the array is not empty, the next element becomes the element at 'index'
        # If the array becomes empty, we stop
        index = (index) % len(arr) if arr else -1
    return index