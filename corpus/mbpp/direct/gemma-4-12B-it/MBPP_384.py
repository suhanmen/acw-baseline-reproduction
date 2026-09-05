def frequency_Of_Smallest(n, arr):
    """
    Finds the frequency of the smallest value in a given array.

    Args:
    n (int): The size of the array (unused in logic, but kept for signature).
    arr (list): The list of integers.

    Returns:
    int: The frequency of the minimum element.
    """
    if not arr:
        return 0

    smallest = min(arr)
    count = 0
    for num in arr:
        if num == smallest:
            count += 1
    return count