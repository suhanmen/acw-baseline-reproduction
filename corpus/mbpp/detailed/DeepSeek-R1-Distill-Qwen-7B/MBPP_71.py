def comb_sort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")
    if len(arr) < 2:
        return arr.copy()

    # Convert to a list of integers if not already
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers.")

    # Initialize the gap
    gap = len(arr) - 1
    # Shrink factor
    shrink_factor = 1.2
    # Create a copy of the array to sort
    sorted_arr = arr.copy()

    while gap > 1:
        # Update the gap size using the shrink factor
        gap = max(1, int(gap / shrink_factor))

        # Perform a single pass with the current gap
        for i in range(len(sorted_arr) - gap):
            if sorted_arr[i] > sorted_arr[i + gap]:
                # Swap elements
                sorted_arr[i], sorted_arr[i + gap] = sorted_arr[i + gap], sorted_arr[i]

    return sorted_arr