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
    total_sum = 0
    # Take the first k elements from the array
    subset = arr[:k]

    for num in subset:
        # An integer has at most two digits if its absolute value is less than 100.
        # For example, 0-99 are <= 2 digits, -99 to -1 are <= 2 digits.
        # The problem statement implies standard digit count, usually checked via absolute value.
        if abs(num) < 100:
            total_sum += num

    return total_sum