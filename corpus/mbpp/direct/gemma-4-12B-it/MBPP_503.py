def add_consecutive_nums(nums):
    """
    Adds consecutive numbers in a list.
    A pair of consecutive numbers are numbers that are numerically 
    adjacent (e.g., x and x+1).

    Looking at the test cases:
    [1, 1, 3, 4, 4, 5, 6, 7] -> [2, 4, 7, 8, 9, 11, 13]
    Indices of consecutive pairs:
    - (1, 1) is not consecutive.
    - (1, 3) is not.
    - (3, 4) are consecutive -> 7 (wait, this doesn't match 2)

    Re-evaluating the pattern from the assertions:
    Example 1: [1, 1, 3, 4, 4, 5, 6, 7] -> [2, 4, 7, 8, 9, 11, 13]
    1+1=2, 1+3=4, 3+4=7, 4+4=8, 4+5=9, 5+6=11, 6+7=13.
    The logic is simply the sum of every pair of adjacent elements in the list.

    Example 2: [4, 5, 8, 9, 6, 10] -> [9, 13, 17, 15, 16]
    4+5=9, 5+8=13, 8+9=17, 9+6=15, 6+10=16.

    Example 3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [3, 5, 7, 9, 11, 13, 15, 17, 19]
    1+2=3, 2+3=5, 3+4=7, 4+5=9, 5+6=11, 6+7=13, 7+8=15, 8+9=17, 9+10=19.

    The function adds adjacent elements in the list.
    """
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] + nums[i+1])
    return result