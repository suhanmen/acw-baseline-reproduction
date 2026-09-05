import math

def _validate_inputs(x: float, y: float) -> None:
    """
    Validates that the inputs are numbers and positive as per requirements.
    Raises ValueError if inputs are not positive numbers.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Inputs must be numeric values.")

    if x <= 0 or y <= 0:
        raise ValueError("Inputs must be positive numbers.")

def _is_even(n: float) -> bool:
    """
    Checks if a number is an even integer.
    Returns True if the number is an integer and divisible by 2.
    """
    if n != int(n):
        return False
    return int(n) % 2 == 0

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # 1. Validate inputs
    _validate_inputs(x, y)

    # 2. Check for degenerate range where start is greater than end
    # The problem states the range is [x, y]. If x > y, the range is empty.
    if x > y:
        return -1

    # 3. Determine the search space.
    # Since we want the "biggest" even integer, we should look starting 
    # from the floor of y downwards.
    # We convert to float to handle potential float inputs, then find the integer floor.
    upper_bound_float = float(y)
    upper_bound_int = int(math.floor(upper_bound_float))

    # 4. Iterate backwards from the floor of y to the ceiling of x.
    # This ensures we find the largest one first.
    lower_bound_int = int(math.ceil(x))

    # We use a loop to find the first even integer starting from the top.
    # This is defensive and avoids complex modulo logic with floating points.
    current_val = upper_bound_int

    # Check if the current value is within the inclusive range [x, y]
    # and if it is even.
    while current_val >= lower_bound_int:
        # Check if current_val is even
        if current_val % 2 == 0:
            # Since we are counting down, the first even we find 
            # is the largest.
            return current_val

        # Decrement to check the next smaller integer
        current_val -= 1

    # 5. If the loop completes without returning, no even integer exists in [x, y]
    return -1