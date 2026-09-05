def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    # The problem description says non-negative, but the examples include negative.
    # In Python, bin(-2) is '-0b10', bin(-3) is '-0b11'.
    # The standard interpretation for 'number of ones' in binary for negative 
    # numbers in these types of challenges usually ignores the sign bit 
    # or treats the integer as a bit pattern. 
    # However, looking at the example [-2, -3, -4, -5, -6] -> [-6, -5, -4, -3, -2],
    # and the logic of "ones in binary", we use bin(x).count('1').

    return sorted(arr, key=lambda x: (bin(x).count('1'), x))