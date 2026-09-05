def binary_search(arr, target):
    """
    Searches for a target element in a sorted array using the binary search algorithm.

    Args:
        arr (list): A sorted list of integers.
        target (int): The integer to search for.

    Returns:
        bool: True if the target is found in the array, False otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == "__main__":
    assert binary_search([1, 2, 3, 5, 8], 6) == False
    assert binary_search([7, 8, 9, 10, 13], 10) == True
    assert binary_search([11, 13, 14, 19, 22, 36], 23) == False