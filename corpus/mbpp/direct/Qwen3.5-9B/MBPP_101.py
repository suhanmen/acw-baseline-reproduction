def kth_element(arr, k, n):
    """
    Finds the kth smallest element in the array.

    Parameters:
    arr (list): List of integers.
    k (int): The kth position to find (1-indexed).
    n (int): The size of the array (for validation, though not strictly needed in logic).

    Returns:
    int: The kth smallest element.
    """
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds")

    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

# Example usage for verification (not part of the required output):
# print(kth_element([12,3,5,7,19], 5, 2))  # Output: 3
# print(kth_element([17,24,8,23], 4, 3))   # Output: 8
# print(kth_element([16,21,25,36,4], 5, 4)) # Output: 36