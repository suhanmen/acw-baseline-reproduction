import math
from typing import List, Union

def sum_squares(lst: List[Union[int, float]]) -> int:
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6

    """
    # Validate that the input is a list
    if not isinstance(lst, list):
        raise TypeError(f"Input must be a list, but received {type(lst).__name__}")

    # Handle the edge case of an empty list immediately
    if not lst:
        return 0

    total_sum: int = 0

    # Iterate through every element in the provided list
    for item in lst:
        # Validate that each element is a number (int or float)
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

        # Step 1: Round each element to the upper integer (Ceiling)
        # math.ceil() returns the smallest integer greater than or equal to x.
        # For example: math.ceil(1.4) -> 2, math.ceil(-2.4) -> -2
        rounded_value: int = math.ceil(item)

        # Step 2: Square the rounded integer
        squared_value: int = rounded_value ** 2

        # Step 3: Accumulate the squared value into the total sum
        total_sum += squared_value

    # Return the final calculated sum
    return total_sum