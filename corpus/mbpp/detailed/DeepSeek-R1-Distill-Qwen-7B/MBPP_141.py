def pancake_sort(arr):
    """
    Sorts a list of elements using pancake sort algorithm.

    Args:
        arr (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.

    Raises:
        ValueError: If the input is not a list of integers.
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers.")
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("All elements must be integers.")

    # Helper function to flip the first k elements of the list
    def flip(k):
        arr[:k] = arr[:k][::-1]
        return arr

    n = len(arr)
    for k in range(n, 0, -1):
        # Find the maximum element in the first k elements
        max_index = 0
        for i in range(k):
            if arr[i] > arr[max_index]:
                max_index = i

        # If the maximum element is not already in place
        if max_index != k - 1:
            # Flip the maximum element to the front
            if max_index != 0:
                flip(max_index + 1)
            flip(k)

    return arr

# Test the function with provided examples
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]