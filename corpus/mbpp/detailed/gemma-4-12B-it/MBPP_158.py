from typing import List

def min_Ops(nums: List[int], n: int, k: int) -> int:
    """
    Finds the minimum number of operations required to make all elements equal.
    In one operation, you can choose any element x and increase it by 1.
    The total sum of elements must remain such that the final equal value
    is reachable given the constraint of the number of operations allowed.

    Wait, let's re-evaluate based on the provided assertions:
    1. [2,2,2,2], n=4, k=3 -> 0. (Already equal, 0 ops needed).
    2. [4,2,6,8], n=4, k=3 -> -1. (Cannot make all equal in 3 ops).
    3. [21,33,9,45,63], n=5, k=6 -> 24.

    Correction on logic analysis:
    The goal is to make all elements equal to some value 'target'.
    Let the current sum be 'current_sum'.
    If we make all elements equal to 'target', the new sum is 'n * target'.
    The number of operations is 'n * target - current_sum'.
    We need to find the minimum non-negative integer 'target' such that:
    1. target >= max(nums)
    2. n * target - current_sum <= k
    3. (n * target - current_sum) is non-negative.

    Actually, let's re-examine assertion 3:
    nums = [21,33,9,45,63], n=5, k=6
    Sum = 21+33+9+45+63 = 171.
    Max = 63.
    If target = 63: Ops = 5 * 63 - 171 = 315 - 171 = 144. 
    This doesn't match 24.

    Let's re-read the standard "minimum operations to make all equal" problem.
    Usually, this involves "decrementing" or "incrementing" values.
    Wait, let's look at the values again.
    Assertion 3: [21,33,9,45,63], n=5, k=6. Result = 24.
    Maybe the operation is: Choose an index i, and decrease nums[i] by 1, 
    and increase nums[j] by 1? No, that's a different problem.

    Let's look at the numbers:
    9, 21, 33, 45, 63.
    Differences: 12, 12, 12, 18.
    If we want to make them equal by "moving" values (decrementing one, incrementing another):
    To make all equal to the median (33):
    9 -> 33 (diff 24)
    21 -> 33 (diff 12)
    33 -> 33 (diff 0)
    45 -> 33 (diff 12)
    63 -> 33 (diff 30)
    Total reduction needed = 24 + 12 + 30 = 66.
    Total increase needed = 24 + 12 = 36.

    Let's look at the difference between max and min:
    63 - 9 = 54.

    Let's try a different logic. Maybe it's the minimum sum of differences 
    to make all elements equal, and k is a constraint on the value of the elements?
    No, "k number of operations".

    Wait, if we look at [21,33,9,45,63] and the target is 33 (the median):
    Sum of differences from median: |21-33| + |33-33| + |9-33| + |45-33| + |63-33|
    = 12 + 0 + 24 + 12 + 30 = 78.

    Let's try another target. If target is the average?
    Sum = 171. Average = 171 / 5 = 34.2.

    Let's look at the number 24 again.
    24 is the difference between 33 and 9.

    Let's re-examine the assertions very carefully.
    min_Ops([2,2,2,2], 4, 3) == 0
    min_Ops([4,2,6,8], 4, 3) == -1
    min_Ops([21,33,9,45,63], 5, 6) == 24

    In assertion 2: [4,2,6,8], n=4, k=3.
    If target is 8: Ops = (8-4)+(8-2)+(8-6)+(8-8) = 4+6+2+0 = 12. 12 > 3.
    If target is 6: Ops = (6-4)+(6-2)+(6-6)+(6-8) ... but we can't decrease.

    If the operation is: "Choose two indices i, j such that nums[i] < nums[j], 
    and increment nums[i] and decrement nums[j]".
    In this case, one operation changes two numbers.
    To make all equal to the median (33) in [21,33,9,45,63]:
    To reach 33:
    9 needs +24
    21 needs +12
    45 needs -12
    63 needs -30
    We can perform operations: 
    Take from 63, give to 9. (30 units)
    Take from 45, give to 21. (12 units)
    Total operations = 30 + 12 = 42. (Not 24).

    Wait! What if the operation is: 
    "Choose index i, nums[i] = nums[i] + 1" AND "Choose index j, nums[j] = nums[j] - 1"
    is ONE operation?
    Then we need to move the "excess" from large numbers to small numbers.
    Excess in [21,33,9,45,63] relative to median 33:
    45 is 12 above.
    63 is 30 above.
    Total excess = 42.
    Total deficit:
    9 is 24 below.
    21 is 12 below.
    Total deficit = 36.
    This doesn't balance.

    Let's try making them equal to some value X.
    Sum must remain constant. 171 / 5 = 34.2. Not an integer.
    If the sum is NOT constant, and we can only increment:
    Then target must be >= max(nums).
    For [4,2,6,8], max=8. Ops = (8-4)+(8-2)+(8-6)+(8-8) = 12. 12 > 3, return -1.
    For [2,2,2,2], max=2. Ops = 0. 0 <= 3, return 0.
    For [21,33,9,45,63], max=63. Ops = (63-21)+(63-33)+(63-9)+(63-45)+(63-63) = 42+30+54+18+0 = 144.
    144 > 6, return -1.

    Something is wrong. Let's look at the numbers again.
    [21,33,9,45,63], n=5, k=6. Result 24.
    Is k the target value?
    If target is 6:
    [21,33,9,45,63] -> all become 6.
    If the operation is "decrement", then ops = (21-6)+(33-6)+(9-6)+(45-6)+(63-6) = 15+27+3+39+57 = 141.

    Wait, let's look at the numbers 21, 33, 9, 45, 63 again.
    They are all multiples of 3? No, 9, 21, 33, 45, 63.
    9 = 3*3
    21 = 3*7
    33 = 3*11
    45 = 3*15
    63 = 3*21

    Wait, what if the operation is:
    Pick two elements, say a and b. Replace them with (a+1) and (b-1).
    The sum is constant. To make all equal, the sum must be divisible by n.
    Sum = 171. 171 / 5 = 34.2. Not possible.

    What if the operation is: 
    Pick an element x, replace with x+1.
    The target must be >= max(nums). 
    The sum increases. 
    Wait, let's look at the numbers again.
    [21,33,9,45,63]. Maybe the target is not max(nums).
    Maybe we can decrease?
    If we can increase and decrease:
    Operation: pick i, j, nums[i]++, nums[j]--.
    This is one operation.
    To make all elements equal to some value X.
    X must be such that n*X = sum(nums).
    But 171 is not divisible by 5.

    What if the operation is: 
    "Pick any element and change it to any other value"
    No, that's usually not "k operations".

    Let's try: 
    Target X. Operations = count of i such that nums[i] != X.
    For [2,2,2,2], n=4, k=3. All equal. Ops = 0. 0 <= 3. Correct.
    For [4,2,6,8], n=4, k=3. 
    If target = 4, ops = 3 (2,6,8). 3 <= 3. So return 3? No, it returns -1.
    If target = 6, ops = 3 (4,2,8). 3 <= 3.
    Wait, if the answer is -1, it means we CANNOT do it in k operations.
    But if we can change any element to any value in 1 op, we could do it in 3 ops.
    So that's not it.

    Let's try:
    One operation: Pick an index i, nums[i] = nums[i] + 1 OR nums[i] = nums[i] - 1.
    For [4,2,6,8], to make all equal to 5:
    |4-5| + |2-5| + |6-5| + |8-5| = 1 + 3 + 1 + 3 = 8.
    To make all equal to 4:
    |4-4| + |2-4| + |6-4| + |8-4| = 0 + 2 + 2 + 4 = 8.

    Let's look at the third assertion again:
    [21,33,9,45,63], n=5, k=6. Result 24.
    Sum = 171. Average = 34.2.
    If we make all elements equal to 34:
    |21-34| + |33-34| + |9-34| + |45-34| + |63-34|
    = 13 + 1 + 25 + 11 + 29 = 80.

    What if the operation is: 
    "Pick an element and change it to any other value".
    Cost is |old - new|.
    Then we want to minimize sum |nums[i] - X| subject to sum |nums[i] - X| <= k.
    If this sum is minimized, we return the minimum sum. 
    If the minimum sum > k, return -1.

    Let's test this logic:
    1. [2,2,2,2], n=4, k=3.
       Min sum |nums[i] - X| is at X = median(2,2,2,2) = 2.
       Sum = 0. 0 <= 3. Return 0