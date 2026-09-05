from typing import List

def rotate_left(nums: List[int], steps: int, extra_steps: int) -> List[int]:
    if len(nums) == 0:
        return nums

    total_steps = steps + extra_steps
    rotation_count = total_steps % len(nums)

    return nums[rotation_count:] + nums[:rotation_count]