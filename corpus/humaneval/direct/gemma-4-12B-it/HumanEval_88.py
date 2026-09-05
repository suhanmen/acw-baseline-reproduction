def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []

    # Create a copy to ensure the original array is not modified
    arr_copy = list(array)

    # Determine the sum of the first and last elements
    # For a single-element array, first and last are the same
    first_val = arr_copy[0]
    last_val = arr_copy[-1]
    total_sum = first_val + last_val

    # Sort based on the parity of the sum
    if total_sum % 2 != 0:
        # Odd sum: sort in ascending order
        arr_copy.sort()
    else:
        # Even sum: sort in descending order
        arr_copy.sort(reverse=True)

    return arr_copy