from typing import List, Any


def is_valid_positive_integer(value: Any) -> bool:
    """
    Checks if a value is an integer and is non-negative.
    Strictly follows the requirement to ignore numbers that 
    are negative or not integers.
    """
    # Check if the type is strictly int (to exclude booleans and floats)
    if not isinstance(value, int) or isinstance(value, bool):
        return False

    # Check if the number is non-negative
    if value < 0:
        return False

    return True


def is_odd(number: int) -> bool:
    """
    Checks if an integer is odd.
    """
    return number % 2 != 0


def calculate_square(number: int) -> int:
    """
    Calculates the square of a number.
    """
    return number * number


def double_the_difference(lst: List[Any]) -> int:
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  

    If the input list is empty, return 0.
    '''
    # Handle edge case: Empty list input
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        return 0

    total_sum_of_squares = 0

    for item in lst:
        # Step 1: Validate the item type and sign.
        # We must ignore non-integers (like floats, strings, None) 
        # and negative integers.
        if not is_valid_positive_integer(item):
            continue

        # Step 2: Check if the valid integer is odd.
        # Note: 0 is even, so it will be skipped by this check.
        if is_odd(item):
            # Step 3: Calculate square of the odd number.
            square_value = calculate_square(item)

            # Step 4: Accumulate to total sum.
            total_sum_of_squares += square_value
        else:
            # Even numbers are ignored as per the "sum of squares of numbers 
            # in the list that are odd" logic.
            pass

    return total_sum_of_squares