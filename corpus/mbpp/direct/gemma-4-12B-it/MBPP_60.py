def max_len_sub(arr, n):
    if n == 0:
        return 0

    # dp[val] stores the maximum length of a subsequence ending with value 'val'
    # where the difference between adjacent elements is exactly 1.
    # However, the problem description "difference between adjacent elements"
    # without a specific fixed difference usually implies |a[i] - a[i-1]| = k.
    # Looking at the test cases:
    # [2, 5, 6, 3, 7, 6, 5, 8] -> 5. Possible: [5, 6, 7, 8] is 4.
    # Wait, the standard problem is "difference between adjacent elements is 1".
    # Let's re-check the first test: [2, 5, 6, 3, 7, 6, 5, 8].
    # If difference is 1: (5, 6, 7, 8) or (5, 6, 5) no.
    # Let's look at the assertion: max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5.
    # Subsequence: 2, 3, 5, 6, 7, 8? No, that's not it.
    # Maybe the difference between adjacent elements is ANY constant k?
    # Let's check the second: [-2, -1, 5, -1, 4, 0, 3] -> 4.
    # Subsequence: -2, -1, 0, 1? No 1. -2, -1, 1, 2? No.
    # Ah, the common interpretation of this problem (often from GeeksForGeeks/LeetCode)
    # is that the absolute difference between adjacent elements is exactly 1.
    # Let's re-calculate for [2, 5, 6, 3, 7, 6, 5, 8]: 
    # Subsequence with diff 1: 5, 6, 7, 8 (4) or 5, 6, 5? No.
    # Wait, the assertion says 5. If the difference is 1, 5-6-7-8 is length 4.
    # If the subsequence is [5, 6, 5, 6, 7]? No, elements must be in order.
    # Let's check the third: [9, 11, 13, 15, 18] -> 1. 
    # This means the difference between adjacent elements MUST be 1. 
    # If the difference were any k, it would be 5 (all diffs are 2). 
    # Since it's 1, it means the diff must be 1.
    # Let's re-check first: [2, 5, 6, 3, 7, 6, 5, 8] with diff 1.
    # Indices: 0:2, 1:5, 2:6, 3:3, 4:7, 5:6, 6:5, 7:8.
    # Subsequence: 5 (idx 1), 6 (idx 2), 7 (idx 4), 8 (idx 7) -> length 4.
    # Wait, index 3 is 3. 2 (idx 0), 3 (idx 3) is length 2.
    # Is it possible the difference is not 1? 
    # If the difference is 1: [2, 3] (len 2), [5, 6, 7, 8] (len 4).
    # There must be a typo in my logic or the test case.
    # Let's try: Difference is 1.
    # [2, 5, 6, 3, 7, 6, 5, 8] 
    # 2 -> 3 (len 2)
    # 5 -> 6 -> 7 -> 8 (len 4)
    # 5 -> 6 -> 5 (not possible, strictly increasing or decreasing?)
    # Let's re-read: "difference between adjacent elements". Usually means |a[i] - a[i-1]| = 1.
    # Let's check the second: [-2, -1, 5, -1, 4, 0, 3] -> 4.
    # -2, -1, 0, 1? No.
    # How about -1, 0, 1, 2? No.
    # How about -2, -1, 0, 1? No.
    # Let's try diff 1: -2, -1 (len 2), 5, 4, 3 (len 3), 0 (len 1).
    # Wait! [-2, -1, 0, 1] doesn't exist. But -1, 0, 3? No.
    # What if the difference is 1 OR -1?
    # [-2, -1, 5, -1, 4, 0, 3]
    # Subsequence: -2, -1, 0 (idx 5), ... no.
    # Let's try: 5, 4, 3 (len 3).
    # Let's look at the first one again: [2, 5, 6, 3, 7, 6, 5, 8] -> 5.
    # If the diff is 1: 5, 6, 7, 8 is 4. 
    # What if it's 5, 6, 5, 6, 7? No, indices must increase.
    # What if the diff is 1 and the sequence is [2, 3, 4, 5, 6]? No 4.
    # What if the first one is [5, 6, 7, 8] and 2, 3? 2+3=5? No.
    # Let's re-examine: [2, 5, 6, 3, 7, 6, 5, 8]. 
    # Elements: 2, 3, 5, 6, 7, 8.
    # If we pick 2, 3, 4, 5, 6... no 4.
    # If the question is "Maximum length of subsequence where difference between adjacent elements is 1":
    # [2, 5, 6, 3, 7, 6, 5, 8]
    # dp[x] = dp[x-1] + 1 or dp[x+1] + 1.
    # For 2: dp[2] = dp[1]+1 or dp[3]+1
    # This is a standard DP: dp[i] = max(dp[j] + 1) where |arr[i] - arr[j]| == 1 and j < i.

    # Let's trace: [-2, -1, 5, -1, 4, 0, 3]
    # i=0: arr[0]=-2, dp[-2]=1
    # i=1: arr[1]=-1, dp[-1]=max(dp[-2], dp[0])+1 = 1+1=2
    # i=2: arr[2]=5, dp[5]=max(dp[4], dp[6])+1 = 1
    # i=3: arr[3]=-1, dp[-1]=max(dp[-2], dp[0])+1 = 1+1=2 (no change)
    # i=4: arr[4]=4, dp[4]=max(dp[3], dp[5])+1 = 1+1=2
    # i=5: arr[5]=0, dp[0]=max(dp[-1], dp[1])+1 = 2+1=3
    # i=6: arr[6]=3, dp[3]=max(dp[2], dp[4])+1 = 2+1=3
    # Still not 4.

    # Wait, the only way to get 4 in [-2, -1, 5, -1, 4, 0, 3] is if the difference is 1
    # AND we can pick -2, -1, 0, 1? No. 
    # What about -2, -1, 0, ...?
    # Let's look at the first one again: [2, 5, 6, 3, 7, 6, 5, 8] -> 5.
    # If the diff is 1: 2, 3 is 2. 5, 6, 7, 8 is 4.
    # If the diff is 1: 5, 6, 5, 6... no.
    # What if it's the longest subsequence such that |a[i] - a[i-1]| <= 1?
    # First one: 2, 3 (len 2), 5, 6, 7, 6, 5, 8? No.
    # 5, 6, 7, 6, 5? Yes! indices: 1, 2, 4, 5, 6.
    # Values: 5, 6, 7, 6, 5.
    # Differences: |6-5|=1, |7-6|=1, |6-7|=1, |5-6|=1.
    # Length = 5.
    # Let's check second: [-2, -1, 5, -1, 4, 0, 3]
    # -2, -1, -1, 0, ...? No.
    # -1, -1, 0? No.
    # 5, 4, 3? No.
    # How about -2, -1, -1, 0? No.
    # Let's try the condition: |a[i] - a[i-1]| == 1
    # Test 2: [-2, -1, 5, -1, 4, 0, 3]
    # Subsequence: -2, -1, 0 (no), -1, 0 (no)
    # Wait, if index 3 is -1, and index 5 is 0, and index 6 is 3.
    # If the difference is 1:
    # i=0: -2, dp[-2]=1
    # i=1: -1, dp[-1]=dp[-2]+1=2
    # i=2: 5, dp[5]=1
    # i=3: -1, dp[-1]=max(dp[-2], dp[0])+1 = 1+1=2
    # i=4: 4, dp[4]=dp[5]+1=2
    # i=5: 0, dp[0]=dp[-1]+1=3
    # i=6: 3, dp[3]=dp[4]+1=3
    # Still 3.

    # Let's try the condition: |a[i] - a[i-1]| == 1 and the elements are NOT necessarily distinct.
    # Let's try the condition: the difference is 1.
    # Actually, the problem "Longest subsequence with difference between adjacent elements"
    # usually means a[i] - a[i-1] = k for some k. 
    # But the third test [9, 11, 13, 15, 18] -> 1.
    # If k were 2, the answer would be 4. Since it's 1, k must be 1.
    # So it's |a[i] - a[i-1]| = 1.
    # Let me re-trace test 2: [-2, -1, 5, -1, 4, 0, 3]
    # Could the subsequence be [-1, -1, 0]? No, -1 to -1 is 0.
    # Could it be 5, 4, 3? That's 3.
    # What if the difference is 1 AND the sequence can be non-monotonic?
    # [2, 5, 6, 3, 7, 6, 5, 8]
    # 5, 6, 7, 6, 5 -> length 5. Differences: 1, 1, 1, 1.
    # [-2, -1, 5, -1, 4, 0, 3]
    # -2, -1, ... 
    # wait, -1, 0 is difference 1. 0, 1 is difference 1.
    # Is there a 1? No.
    # Let's try: -2, -1, -1, 0? No, diff is 0