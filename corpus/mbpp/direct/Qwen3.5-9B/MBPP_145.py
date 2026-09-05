from typing import Tuple, Union

def max_Abs_Diff(arr: Tuple[Union[int, float], ...], n: Union[int, float]) -> Union[int, float]:
    if n == 0:
        return 0
    nums = list(arr)
    if len(nums) == 0:
        return 0
    nums.sort()
    if len(nums) > 0:
        result = nums[-1] - nums[0]
        if n > 0 and len(nums) > n:
            return nums[-1] - nums[0]
        return nums[-1] - nums[0]
    return 0

assert max_Abs_Diff((2,1,5,3),4) == 4
assert max_Abs_Diff((9,3,2,5,1),5) == 8
assert max_Abs_Diff((3,2,1),3) == 2