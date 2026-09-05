def max_Abs_Diff(arr, n):
    """
    Finds the maximum difference between any two elements in a given array.
    The maximum absolute difference in an array is simply the difference
    between the maximum and minimum elements.
    """
    if not arr or n == 0:
        return 0

    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]

    return max_val - min_val

if __name__ == "__main__":
    assert max_Abs_Diff((2,1,5,3), 4) == 4
    assert max_Abs_Diff((9,3,2,5,1), 5) == 8
    assert max_Abs_Diff((3,2,1), 3) == 2