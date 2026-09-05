def check_greater(arr, num):
    """
    Checks whether the entered number is greater than all elements of the given array.
    Returns 'Yes, the entered number is greater than those in the array' if true,
    otherwise returns 'No, entered number is less than those in the array'.
    """
    if all(num > x for x in arr):
        return 'Yes, the entered number is greater than those in the array'
    else:
        return 'No, entered number is less than those in the array'