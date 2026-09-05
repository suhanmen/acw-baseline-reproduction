def longest_subseq_with_diff_one(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # dp[x] = length of longest subsequence ending with value x
    # We use a dictionary to map value -> length
    dp = {}

    # We also need to reconstruct the logic: 
    # For each number, we can extend a sequence ending with x-1 or x+1
    # But note: the problem asks for a subsequence (not necessarily contiguous)
    # such that adjacent elements in the subsequence differ by exactly 1.
    # However, the examples suggest we are looking for the longest path in a graph 
    # where edges exist between adjacent values (i.e., x and x+1) and we can only 
    # use each index once, and the sequence must be in the original order.

    # Actually, re-reading the problem: "longest subsequence" typically means we pick 
    # indices i1 < i2 < ... < ik such that |arr[i_j] - arr[i_{j+1}]| == 1.
    # But the examples: 
    # [1,2,3,4,5,3,2] -> 6: likely 1,2,3,4,5,4 or 1,2,3,4,5,6? But 6 is not there. 
    # Wait, the example says 6. Let's see: 1,2,3,4,5,4 -> length 6? But 4 appears again. 
    # Or 2,3,4,5,3,2 -> length 6? Yes, that works: indices 1,2,3,4,5,6 (0-indexed: 1,2,3,4,5,6) 
    # values: 2,3,4,5,3,2 -> differences are 1. So length 6.

    # So we need to find the longest subsequence (by index) such that consecutive elements 
    # in the subsequence have absolute difference 1.

    # We can use dynamic programming: 
    # Let dp[i] = length of the longest subsequence ending at index i.
    # Then dp[i] = 1 + max(dp[j]) for all j < i such that |arr[i] - arr[j]| == 1.
    # If no such j exists, dp[i] = 1.

    # Time complexity: O(n^2). Since n is not specified but the examples are small, 
    # and the problem does not specify constraints, we assume O(n^2) is acceptable.

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    return max(dp) if n > 0 else 0

# Test the function with the provided assertions
# assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
# assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
# assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7

# But note: the third example: [1,2,3,2,3,7,2,1] -> 7
# Let's trace: 
# One possible: 1 (index0), 2 (index1), 3 (index2), 2 (index3), 3 (index4), 2 (index6), 1 (index7) -> length 7? 
# Check differences: 
# 1->2:1, 2->3:1, 3->2:1, 2->3:1, 3->2:1, 2->1:1 -> yes. 
# So the function should return 7.

# However, the above O(n^2) solution should work.

# But wait: the problem says "difference between adjacents is one" -> meaning absolute difference is 1.

# Let's run the logic mentally on the first example:
# arr = [1,2,3,4,5,3,2]
# dp[0]=1 (1)
# dp[1]=2 (1,2)
# dp[2]=3 (1,2,3)
# dp[3]=4 (1,2,3,4)
# dp[4]=5 (1,2,3,4,5)
# dp[5]: can extend from 4 (index3) -> 5, so 4+1=5; also from 2 (index6? no, j<5) -> from index3:4->3? no, |3-4|=1 -> yes, so 4+1=5; 
#        also from index1:2->3? |3-2|=1 -> so 2+1=3 -> max is 5? but wait, we can also do 1,2,3,4,3 -> length 5? 
#        but the example says 6. 
#        How to get 6? 
#        Consider: 2 (index1), 3 (index2), 4 (index3), 5 (index4), 3 (index5), 2 (index6) -> length 6.
#        So for index6 (value 2): 
#          j=5 (value3): |2-3|=1 -> dp[5]+1 = 5+1=6? 
#          j=1 (value2): |2-2|=0 -> skip.
#        So we need dp[5] to be 5? 
#        How to get dp[5]=5: 
#          from index4 (5): |3-5|=2 -> no.
#          from index3 (4): |3-4|=1 -> dp[3]=4 -> 4+1=5.
#        So dp[5]=5 (sequence: 1,2,3,4,3) or (2,3,4,5,3) but 5 is at index4 and 3 at index5: yes, 2,3,4,5,3 -> indices 1,2,3,4,5 -> length 5.
#        Then dp[6]: from index5 (3): |2-3|=1 -> 5+1=6.
#        So yes, it works.

# Therefore, the O(n^2) solution is correct.

# But note: the problem says "adjacents" meaning in the subsequence, not in the array. So our interpretation is correct.

# However, the above code does not use the 'n' parameter meaningfully? 
# The function signature is longest_subseq_with_diff_one(arr, n) and n is the length of arr.
# We can ignore n and use len(arr), but to be safe, we can use n as the length.

# Revised code to use n:

def longest_subseq_with_diff_one(arr, n):
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    return max(dp)

# But note: the problem says "Your function must satisfy these assertions", so we write the function as required.

# However, the above solution is O(n^2). If n is large, we might need optimization, but the problem does not specify constraints and the examples are small.

# Let's output the function as required.