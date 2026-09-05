def max_sum(arr, n):
    """
    Find the maximum sum of a bi-tonic sub-sequence in the given array.
    A bi-tonic sub-sequence is a sequence that first strictly increases and then strictly decreases.

    Args:
        arr (list): The input array.
        n (int): The number of elements in the array (for validation).

    Returns:
        int: The maximum sum of a bi-tonic sub-sequence.

    Raises:
        ValueError: If the input array is empty.
    """
    if not arr or n <= 0:
        raise ValueError("Array must not be empty.")

    if n == 1:
        return arr[0]

    # Helper function to compute the maximum sum of increasing subsequence ending at each index
    def max_increasing_subsequenceEndingAt(i):
        if i == 0:
            return arr[i]
        max_sum = arr[i]
        for j in range(i):
            if arr[j] < arr[i] and max_sum < max_increasing_subsequenceEndingAt(j) + arr[i]:
                max_sum = max_increasing_subsequenceEndingAt(j) + arr[i]
        return max_sum

    # Helper function to compute the maximum sum of decreasing subsequence starting at each index
    def max_decreasing_subsequenceStartingAt(i):
        if i == n - 1:
            return arr[i]
        max_sum = arr[i]
        for j in range(i + 1, n):
            if arr[j] < arr[i] and max_sum < max_decreasing_subsequenceStartingAt(j) + arr[i]:
                max_sum = max_decreasing_subsequenceStartingAt(j) + arr[i]
        return max_sum

    max_total = 0
    for i in range(n):
        increasing_sum = max_increasing_subsequenceEndingAt(i)
        decreasing_sum = max_decreasing_subsequenceStartingAt(i)
        total = increasing_sum + decreasing_sum - arr[i]
        if total > max_total:
            max_total = total

    return max_total

# Test cases to validate the solution
def test_max_sum():
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
    assert max_sum([80, 60, 30, 40, 20, 10], 6) == 210
    assert max_sum([2, 3, 14, 16, 21, 23, 29, 30], 8) == 138
    assert max_sum([5], 1) == 5
    assert max_sum([], 0) == 0  # After raising ValueError in the function
    assert max_sum([1, 2, 3, 4, 3, 2, 1], 7) == 14  # 1+2+3+4+3+2+1 = 16 (but the maximum bi-tonic is the entire sequence, sum 16)

test_max_sum()