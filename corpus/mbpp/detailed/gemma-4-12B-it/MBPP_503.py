from typing import List

def add_consecutive_nums(numbers: List[int]) -> List[int]:
    """
    Adds consecutive numbers in a list. 
    Consecutive numbers are defined as numbers that differ by exactly 1 
    from the previous number in the sequence.

    Example:
    [1, 1, 3, 4, 4, 5, 6, 7]
    - 1, 1 are not consecutive.
    - 3, 4 are consecutive -> 7
    - 4, 4 are not consecutive.
    - 4, 5, 6, 7 are consecutive -> 4+5=9, 5+6=11, 6+7=13
    Wait, the example logic is: Sum each pair of numbers that are 
    numerically consecutive (x and x+1).

    Let's re-examine the example:
    Input: [1, 1, 3, 4, 4, 5, 6, 7]
    Pairs:
    (1, 1) -> No
    (1, 3) -> No
    (3, 4) -> Yes (3+4=7)
    (4, 4) -> No
    (4, 5) -> Yes (4+5=9)
    (5, 6) -> Yes (5+6=11)
    (6, 7) -> Yes (6+7=13)

    Wait, let's look at the output: [2, 4, 7, 8, 9, 11, 13]
    The example outputs are actually summing consecutive indices if they 
    satisfy a specific condition? Let's re-evaluate the sums.

    Example 1: [1, 1, 3, 4, 4, 5, 6, 7] -> [2, 4, 7, 8, 9, 11, 13]
    1+1=2
    1+3=4
    3+4=7
    4+4=8
    4+5=9
    5+6=11
    6+7=13

    It appears the rule is: Sum every two adjacent elements in the list 
    regardless of their value.

    Example 2: [4, 5, 8, 9, 6, 10] -> [9, 13, 17, 15, 16]
    4+5=9
    5+8=13
    8+9=17
    9+6=15
    6+10=16

    Example 3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [3, 5, 7, 9, 11, 13, 15, 17, 19]
    1+2=3
    2+3=5
    3+4=7
    4+5=9
    5+6=11
    6+7=13
    7+8=15
    8+9=17
    9+10=19

    The logic is: Given a list of N numbers, return a list of N-1 numbers 
    where each element at index i is the sum of elements at index i and i+1.
    """

    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    # Validate elements are integers
    for item in numbers:
        if not isinstance(item, int):
            raise ValueError("All elements in the list must be integers.")

    # Handle edge case: empty list
    if len(numbers) == 0:
        return []

    # Handle edge case: single element list
    # The sum of adjacent elements requires at least two elements.
    if len(numbers) == 1:
        return []

    result_sums: List[int] = []

    # Iterate through the list up to the second to last element
    # We use range(len(numbers) - 1) to ensure we always have an i+1
    num_iterations = len(numbers) - 1

    for i in range(num_iterations):
        current_value = numbers[i]
        next_value = numbers[i + 1]

        # Perform the addition
        pair_sum = current_value + next_value

        # Append the result to our collection
        result_sums.append(pair_sum)

    return result_sums