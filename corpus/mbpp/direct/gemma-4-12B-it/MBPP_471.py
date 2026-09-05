def find_remainder(arr, length, n):
    """
    Finds the remainder of the product of the first 'length' elements
    of array 'arr' when divided by 'n'.
    """
    remainder = 1
    for i in range(length):
        remainder = (remainder * arr[i]) % n
    return remainder