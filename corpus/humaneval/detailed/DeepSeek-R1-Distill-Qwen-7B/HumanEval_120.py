def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]
    """
    # Handle edge cases
    if not arr or k == 0:
        return []
    if k == len(arr):
        return sorted(arr)
    if k == 1:
        return [max(arr)]

    # Sort the array to easily find the k largest elements
    sorted_arr = sorted(arr)

    # Get the k largest elements
    top_k = sorted_arr[-k:]

    # Return the result as a list
    return top_k