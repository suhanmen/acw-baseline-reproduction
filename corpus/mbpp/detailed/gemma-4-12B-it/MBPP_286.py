from typing import List

def max_sub_array_sum_repeated(arr: List[int], k: int, n: int) -> int:
    """
    Finds the largest sum of a contiguous subarray in an array formed by
    repeating the input 'arr' a total of 'k' times.

    The logic follows these principles:
    1. If k == 1, the problem is a standard Maximum Subarray Sum (Kadane's).
    2. If k > 1, we need to consider that the maximum sum could span
       across multiple repetitions.
    3. However, if the total sum of the array is positive, the maximum sum
       might involve taking all elements of several repetitions plus a prefix
       and/or suffix of another repetition.
    4. If the total sum of the array is non-positive, the maximum sum is 
       bounded by the max subarray sum within a span of up to 2 repetitions 
       (since we can't benefit from full cycles of negative sums).
    """

    # --- Input Validation ---
    if not isinstance(arr, list):
        raise ValueError("Input 'arr' must be a list of integers.")
    if not isinstance(k, int) or not isinstance(n, int):
        raise ValueError("Parameters 'k' and 'n' must be integers.")
    if k <= 0:
        raise ValueError("Parameter 'k' (repeats) must be greater than 0.")
    if n <= 0:
        raise ValueError("Parameter 'n' (limit) must be greater than 0.")

    # The problem states "repeating the given array k times".
    # Usually, 'n' in such competitive programming contexts refers to the limit
    # of repetitions or a specific constraint, but the assertions suggest
    # 'n' might be the number of repetitions allowed or a specific limit.
    # Looking at the assertions:
    # ([10, 20, -30, -1], 4, 3) -> repeat 4 times, limit 3? 
    # Wait, the signature suggests (arr, k, n). 
    # Let's analyze the assertions to infer the meaning of k and n.
    # assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    #   Sum of [10, 20] is 30. If repeated 4 times: [10,20,-30,-1, 10,20,-30,-1, ...]
    #   Max sum is 30.
    # assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    #   [-1, 10, 20] repeated 3 times: [-1, 10, 20, -1, 10, 20, -1, 10, 20]
    #   Sum of all 3 repeats: (-1+10+20) * 3 = 31 * 3 = 93.
    #   Wait, 59 is (10+20) + (-1+10+20) + (10+20) = 30 + 31 + 30 = 91? No.
    #   Let's re-evaluate 59: (-1+10+20) + (-1+10+20) + (-1+10+20) = 93.
    #   If we take [10, 20, -1, 10, 20] from the middle: 10+20-1+10+20 = 59.
    #   This is a subarray of the repeated sequence.
    #   In this case, k=3 (repeats), n=2 (something else?).
    #   Actually, let's look at the third assertion:
    #   max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
    #   This is the max element.

    # Re-interpreting the parameters based on common patterns:
    # k = number of repetitions.
    # n = ? If the assertions are correct:
    # 1. ([10, 20, -30, -1], 4, 3) -> k=4, n=3. Max sum 30.
    #    The sum of one array is 10+20-30-1 = -1.
    #    Since total sum is negative, we don't want to repeat the whole array.
    #    Max subarray is [10, 20] = 30.
    # 2. ([-1, 10, 20], 3, 2) -> k=3, n=2. Max sum 59.
    #    Sum of one array is -1+10+20 = 29.
    #    Total sum is positive (29).
    #    With k=3 repetitions, total sum = 29 * 3 = 87.
    #    Wait, 59... If we use n=2 as the "max length" or "limit"?
    #    If n=2 means we can take at most 2 full repetitions? 29 * 2 = 58.
    #    58 + 10 (from next) = 68? No.
    #    Wait: 29 (first) + 29 (second) + 1 (from first part of third)? 29+29+1=59.
    #    Actually, 10+20 + (-1+10+20) + (10+20) = 30 + 31 + 30 = 91.
    #    Let's look at 59 again. 10+20 (from seq 1) + (-1+10+20) (seq 2) + 10 (from seq 3)? 
    #    No, that's not contiguous.
    #    Contiguous: [10, 20, -1, 10, 20] = 59.
    #    This uses part of seq 1, all of seq 2, and part of seq 3.
    #    This is 3 repetitions. What is n=2?
    #    Maybe n is the max number of elements to take from the "ends"?
    #    Or maybe n is the max number of "full" repetitions?
    #    If k=3 and n=2, and total sum is positive:
    #    Sum = (n * total_sum) + max_subarray_sum_of_extended_array?
    #    Let's try: total_sum = 29. n=2. 29 * 2 = 58.
    #    Then we need 1 more to get 59.
    #    If we take the repeated array: [-1, 10, 20, -1, 10, 20, -1, 10, 20]
    #    Subarrays: [10, 20, -1, 10, 20] = 59.
    #    This uses elements from 3 repetitions.

    # Let's re-read: "largest sum of contiguous array in the modified array 
    # which is formed by repeating the given array k times".
    # The 'n' is likely the number of repetitions we can use.
    # Wait, the parameters are (arr, k, n).
    # Looking at Assertion 1: arr=[10, 20, -30, -1], k=4, n=3. Max sum 30.
    # Assertion 2: arr=[-1, 10, 20], k=3, n=2. Max sum 59.
    # Assertion 3: arr=[-1, -2, -3], k=3, n=3. Max sum -1.

    # In Assertion 1: k=4 (repeats), n=3 (limit?). Total sum = -1. 
    # Since sum <= 0, max sum is Kadane on (arr + arr).
    # In Assertion 2: k=3 (repeats), n=2 (limit?). Total sum = 29.
    # Since sum > 0, max sum = (n * total_sum) + (max subarray sum of a special construction).
    # If we use n=2 repetitions fully: 2 * 29 = 58.
    # Then we look for the max subarray sum in (arr + arr) but we can only 
    # pick parts that connect to the start and end.
    # Actually, the formula for max sum of k repeats when sum > 0 is:
    # MaxSum = (k-1) * total_sum + MaxSubarraySum(arr + arr)
    # Let's check:
    # Assert 1: k=4, total_sum=-1. (Sum <= 0).
    # Kadane on (arr + arr): [10, 20, -30, -1, 10, 20, -30, -1] -> 30. Correct!
    # Assert 2: k=3, total_sum=29. (Sum > 0).
    # Formula: (k-1) * total_sum + MaxSubarraySum(arr + arr)
    # MaxSubarraySum([-1, 10, 20, -1, 10, 20]) -> [10, 20, -1, 10, 20] = 59.
    # (3-1) * 29 + MaxSubarraySum([-1, 10, 20, -1, 10, 20]) = 58 + ? 
    # That doesn't match 59.

    # Let's try another formula for sum > 0:
    # MaxSum = (k-n) * total_sum + MaxSubarraySum(arr repeated n times)? No.
    # Let's try: MaxSum = (k-1) * total_sum + MaxSubarraySum(arr + arr)
    # If k=3, n=2? Maybe n is the number of repetitions to use in the Kadane part?
    # If n=2, then k-n = 3-2 = 1.
    # MaxSum = (k-n) * total_sum + MaxSubarraySum(arr repeated n times).
    # Assert 2: k=3, n=2. total_sum=29.
    # MaxSum = (3-2) * 29 + MaxSubarraySum([-1, 10, 20, -1, 10, 20])
    # MaxSubarraySum([-1, 10, 20, -1, 10, 20]) = 59.
    # MaxSum = 29 + 59 = 88. Still not 59.

    # Wait! If n is the number of repetitions allowed, and k is... something else?
    # Let's look at the numbers again.
    # Assert 2: arr=[-1, 10, 20], k=3, n=2. Result 59.
    # Max Subarray of repeated arr (3 times): [-1, 10, 20, -1, 10, 20, -1, 10, 20]
    # Subarrays: [10, 20, -1, 10, 20] = 59.
    # [10, 20, -1, 10, 20, -1, 10, 20] = 80.
    # [ -1, 10, 20, -1, 10, 20, -1, 10, 20] = 87.
    # If the result is 59, it means we can only use a limited number of elements?
    # Or is n the number of repetitions? 
    # If k=3 (total repeats) and n=2 (max repeats to use in the sum)?
    # If we are allowed to use at most n repetitions:
    # Assert 2: k=3, n=2. We use at most 2 repeats.
    # Max Subarray of [-1, 10, 20, -1, 10, 20] is 59. Correct!
    # Assert 1: k=4, n=3. We use at most 3 repeats.
    # Max Subarray of [10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1]
    # Kadane gives 30. Correct!
    # Assert 3: k=3, n=3. We