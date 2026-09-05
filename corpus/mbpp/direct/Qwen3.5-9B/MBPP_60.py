from typing import List

def max_len_sub(arr: List[int], diff: int) -> int:
    if not arr:
        return 0

    # Map each number to the length of the longest subsequence ending at that number
    dp = {}
    max_length = 1

    for x in arr:
        prev_len = dp.get(x - diff, 0)
        current_len = prev_len + 1
        dp[x] = max(dp.get(x, 0), current_len)
        if current_len > max_length:
            max_length = current_len

    return max_length