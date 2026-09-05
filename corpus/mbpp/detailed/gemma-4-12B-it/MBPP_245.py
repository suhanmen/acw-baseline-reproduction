from typing import List


def max_sum_bitonic_subsequence(arr: List[int], n: int) -> int:
    """
    Finds the maximum sum of a bi-tonic subsequence in a given array.
    A bi-tonic subsequence is a sequence that first strictly increases
    and then strictly decreases.

    Example: [1, 15, 51, 45, 33, 100, 12, 18, 9]
    A bi-tonic subsequence could be [1, 15, 51, 100, 18, 9].

    Args:
        arr: A list of integers.
        n: The number of elements in the list.

    Returns:
        The maximum sum of a bi-tonic subsequence.
    """
    # Input Validation
    if not isinstance(arr, list):
        raise ValueError("Input 'arr' must be a list.")

    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    if len(arr) != n:
        raise ValueError("The length of 'arr' must equal the provided value 'n'.")

    # Handle empty or single element cases
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # msis[i] will store the maximum sum of an increasing subsequence 
    # ending at index i.
    msis = [0] * n

    # msds[i] will store the maximum sum of a decreasing subsequence 
    # starting at index i (which is equivalent to an increasing subsequence 
    # ending at index i if we scan from right to left).
    msds = [0] * n

    # Initialize base cases for MSIS
    # Every element is an increasing subsequence of itself.
    for i in range(n):
        msis[i] = arr[i]

    # Compute Maximum Sum Increasing Subsequence (MSIS)
    # For each element at index i, check all previous elements at index j.
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                current_sum = msis[j] + arr[i]
                if current_sum > msis[i]:
                    msis[i] = current_sum

    # Initialize base cases for MSDS
    # Every element is a decreasing subsequence of itself.
    for i in range(n):
        msds[i] = arr[i]

    # Compute Maximum Sum Decreasing Subsequence (MSDS)
    # Scanning from right to left. For each element at index i, 
    # check all elements at index j to its right.
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                current_sum = msds[j] + arr[i]
                if current_sum > msds[i]:
                    msds[i] = current_sum

    # The maximum bi-tonic sum at index i is (MSIS[i] + MSDS[i] - arr[i])
    # We subtract arr[i] because it is included in both the increasing
    # and decreasing sums at the peak.
    max_bitonic_sum = 0
    for i in range(n):
        # A bi-tonic sequence can be strictly increasing, 
        # strictly decreasing, or both.
        # The logic (msis[i] + msds[i] - arr[i]) covers all three.
        current_bitonic_sum = msis[i] + msds[i] - arr[i]
        if current_bitonic_sum > max_bitonic_sum:
            max_bitonic_sum = current_bitonic_sum

    return max_bitonic_sum


def max_sum(arr: List[int], n: int) -> int:
    """
    Wrapper function to match the required signature.
    """
    return max_sum_bitonic_subsequence(arr, n)