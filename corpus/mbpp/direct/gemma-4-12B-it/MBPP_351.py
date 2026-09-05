def first_Element(arr, n, k):
    """
    Finds the first element in the array that occurs at least k times.

    Args:
    arr (list): The input list of elements.
    n (int): The number of elements in the list.
    k (int): The required frequency of the element.

    Returns:
    The first element that appears k or more times, or None if no such element exists.
    """
    counts = {}
    # First pass: count occurrences of each element
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    # Second pass: find the first element in the original array that meets the count
    for x in arr:
        if counts[x] >= k:
            return x
    return None

if __name__ == "__main__":
    assert first_Element([0,1,2,3,4,5],6,1) == 0
    assert first_Element([1,2,1,3,4],5,2) == 1
    assert first_Element([2,3,4,3,5,7,1,2,3,5],10,2) == 2