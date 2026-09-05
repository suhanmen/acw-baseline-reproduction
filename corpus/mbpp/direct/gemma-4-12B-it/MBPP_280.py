def sequential_search(arr, target):
    """
    Searches for a target element in an array using the sequential search algorithm.

    Args:
        arr (list): The list of elements to search through.
        target: The element to find.

    Returns:
        tuple: (True, index) if the target is found, (False, -1) otherwise.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return (True, index)
    return (False, -1)

if __name__ == "__main__":
    assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)