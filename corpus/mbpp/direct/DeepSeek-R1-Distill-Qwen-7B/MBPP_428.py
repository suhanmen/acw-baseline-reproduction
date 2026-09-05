def shell_sort(arr):
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    n = len(arr)
    gap = n // 2  # Starting gap value

    # Continue sorting with smaller gaps until gap is 0
    while gap > 0:
        # Perform a gap insertion sort for the current gap
        for i in range(gap, n):
            # Insert arr[i] into the correct position in the subarray arr[0..i-gap]
            temp = arr[i]
            j = i - gap
            while j >= 0 and temp < arr[j]:
                arr[j + gap] = arr[j]  # Move the larger element to the right
                j -= gap
            arr[j + gap] = temp  # Place the element at its correct position
        gap = gap // 2  # Reduce the gap to the next lower value

    return arr