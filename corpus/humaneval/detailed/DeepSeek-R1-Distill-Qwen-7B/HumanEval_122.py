def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # If the array is empty, return 0
    if not arr or k <= 0 or k > len(arr):
        return 0

    total = 0
    for i in range(min(k, len(arr))):
        num = abs(arr[i])
        # Check if the number has at most two digits
        if len(str(num)) <= 2:
            total += num

    return total