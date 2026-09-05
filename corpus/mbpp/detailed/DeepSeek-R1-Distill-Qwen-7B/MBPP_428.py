def shell_sort(arr):
    """
    Sort the input list using the shell sort algorithm.
    """
    # Handle empty input
    if not isinstance(arr, list) or len(arr) == 0:
        return []

    # Make a copy to avoid modifying the original list
    data = arr.copy()

    # Function to determine the gap sequence
    def get_gaps(n):
        gaps = []
        while n > 1:
            gaps.append(n)
            n = n // 2
        return gaps

    # Get the initial gap sequence
    gaps = get_gaps(len(data))

    for gap in gaps:
        for i in range(gap, len(data)):
            current_value = data[i]
            j = i - gap
            # Perform insertion sort for each gap
            while j >= 0 and current_value < data[j]:
                data[j + gap] = data[j]
                j -= gap
            data[j] = current_value

    return data