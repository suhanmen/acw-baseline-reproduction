def sort_array(arr):
    """
    Sort an array of non-negative integers based on the number of ones in their binary representation
    and their decimal value for tie-breakers.
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))