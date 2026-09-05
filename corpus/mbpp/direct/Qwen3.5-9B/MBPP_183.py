from typing import List

def count_pairs(nums: List[int], k: int) -> int:
    if k < 0:
        return 0
    seen = set()
    count = 0
    for num in nums:
        if k == 0:
            if (num, 1) in seen:
                count += seen[(num, 1)]
            seen[(num, 1)] = seen.get((num, 1), 0) + 1
        else:
            if (num - k, 1) in seen:
                count += seen[(num - k, 1)]
            if (num + k, 1) in seen:
                count += seen[(num + k, 1)]
            seen[num] = 1
    return count