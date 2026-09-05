def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum of the first and last element is odd,
    or in descending order if the sum is even. The original array is not modified.

    Edge cases:
    - If the array is empty, return it immediately.
    - If the array has a single element, return it as is.

    Parameters:
    array (list): The input list of non-negative integers.

    Returns:
    list: A sorted copy of the input array based on the given condition.
    """
    if not array:
        return []
    if len(array) == 1:
        return array.copy()  # Return a copy to avoid modifying the original

    first = array[0]
    last = array[-1]
    sum_first_last = first + last

    # Create a copy of the array to avoid modifying the original
    sorted_array = array.copy()

    if sum_first_last % 2 == 1:
        # Sort in ascending order
        sorted_array.sort()
    else:
        # Sort in descending order
        sorted_array.sort(reverse=True)

    return sorted_array