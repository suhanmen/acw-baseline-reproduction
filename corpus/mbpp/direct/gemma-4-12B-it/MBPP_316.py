def find_last_occurrence(arr, target):
    """
    Finds the index of the last occurrence of a given number in an array.
    Note: While the problem description mentions a 'sorted' array, the 
    provided assertions show arrays that are not strictly sorted (e.g., 
    [2, 3, 5, 8, 6, 6, 8, 9, 9, 9] and [2, 2, 1, 5, 6, 6, 6, 9, 9, 9]).
    Therefore, a linear scan from right to left is the correct general solution.
    """
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
    assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
    assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6