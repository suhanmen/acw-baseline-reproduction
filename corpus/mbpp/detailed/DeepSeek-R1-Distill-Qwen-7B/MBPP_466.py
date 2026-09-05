def find_peak(arr):
    """
    Finds the peak element in the given array.

    An element is considered a peak if it is greater than its neighbors.
    If all elements are equal, returns 0 as a default peak index.

    Parameters:
        arr (list): The input array to find the peak in.

    Returns:
        int: The index of a peak element.

    Raises:
        ValueError: If the input array is empty.
    """
    # Handle the case of an empty array
    if not arr:
        raise ValueError("Empty array has no peak element.")

    # If there's only one element, it's the peak
    if len(arr) == 1:
        return 0

    # Iterate through the array starting from the second element
    for i in range(1, len(arr) - 1):
        current = arr[i]
        prev = arr[i-1]
        next_element = arr[i+1]

        if current > prev and current > next_element:
            return i

    # If we're here, check the boundaries
    # Check if the first element is a peak
    if arr[0] >= arr[1]:
        return 0

    # Check if the last element is a peak
    if arr[-1] >= arr[-2]:
        return len(arr) - 1

    # If all elements are equal, return 0 as a default
    return 0