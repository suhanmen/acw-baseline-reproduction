import math

def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    # Step 1: Validate input types.
    # The problem implies x and n should be numeric (int or float).
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        return False

    # Step 2: Handle the case where x is 1.
    # Any non-zero n raised to the power of 0 is 1.
    # Based on the example is_simple_power(1, 4) => true, 
    # x=1 is a simple power for any n != 0.
    if x == 1:
        # Special case: 0**0 is mathematically indeterminate, 
        # but in many programming contexts (including Python's pow), 
        # 0**0 is 1. However, usually, n=0 is handled specifically.
        if n == 0:
            # Depending on interpretation, 0**int = 1 only if int=0.
            # Given the logic of "simple power", we consider x=1 a power of n.
            return True
        return True

    # Step 3: Handle the case where n is 0.
    # 0**int is 0 (for int > 0) or 1 (for int = 0).
    if n == 0:
        # x=1 was handled above. If x is anything else, it's only possible if x=0.
        if x == 0:
            return True
        return False

    # Step 4: Handle the case where n is 1.
    # 1**int is always 1.
    if n == 1:
        # x=1 was handled above. If x is not 1, it cannot be a power of 1.
        return x == 1

    # Step 5: Handle negative numbers and zero for x.
    # If x is 0 and n is not 0, x cannot be a power of n (unless n is 0, handled).
    if x == 0:
        return False

    # If n is negative, the result x could be negative or positive.
    # If n is positive and x is negative, x cannot be a power of n.
    if n > 0 and x < 0:
        return False

    # Step 6: Iterative Check for Integer Power.
    # To be "simple", x must be n^k for some integer k >= 0.
    # We use a loop to multiply n by itself until we reach or exceed |x|.
    # This avoids floating point precision issues with logarithms.

    current_value = 1

    # We use the absolute value for comparison logic to handle negative bases.
    # If n is negative, the signs will alternate: n^0=1, n^1=n, n^2=n^2, etc.

    # We check powers k = 0, 1, 2, ...
    # Since x is a finite number, this loop will eventually terminate.

    # Loop limit: if |current_value| exceeds |x| and |n| > 1, 
    # it's impossible to reach x by further multiplication.

    # Special check for n = -1 (which would result in 1 or -1).
    if n == -1:
        return x == 1 or x == -1

    # Standard iterative approach for |n| > 1.
    # We need to handle the magnitude to ensure we don't loop infinitely.
    # If |n| > 1, current_value grows exponentially.

    # Check k=0
    if current_value == x:
        return True

    # Check k=1, 2, ...
    # We use a loop that continues as long as the magnitude of current_value
    # is less than or equal to the magnitude of x.

    temp_val = n
    while abs(temp_val) <= abs(x) if x != 0 else False:
        if temp_val == x:
            return True

        # Calculate next power
        next_val = temp_val * n

        # Check for overflow/infinite loop if n is 1 or -1 (already handled)
        # or if current_val stops changing.
        if next_val == temp_val:
            break

        temp_val = next_val

        # Safety break: if the magnitude grows beyond x and we haven't hit it.
        if abs(temp_val) > abs(x) and (temp_val * n) != x:
            # One last check for the very next multiplication to cover sign flips
            if temp_val * n == x:
                return True
            break

    return False