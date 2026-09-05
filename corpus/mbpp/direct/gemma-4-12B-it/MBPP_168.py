def frequency(arr, num):
    """
    Finds the frequency of a number in a given array.

    Args:
        arr (list): A list of numbers.
        num (int/float): The number to find the frequency of.

    Returns:
        int: The number of occurrences of num in arr.
    """
    count = 0
    for item in arr:
        if item == num:
            count += 1
    return count

if __name__ == "__main__":
    assert frequency([1,2,3],4) == 0
    assert frequency([1,2,2,3,3,3,4],3) == 3
    assert frequency([0,1,2,3,1,2],1) == 2