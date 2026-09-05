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
    # Handle cases where n is 0
    if n == 0:
        return x == 0  # 0^k is 0 for k > 0, but 0^0 is undefined

    # Handle cases where x is 1, since 1 can be n^0 for any n !=0
    if x == 1:
        return n != 0  # since 0^0 is undefined

    # Handle cases where x is 0
    if x == 0:
        return n == 0  # only 0^1 is 0, but 0^0 is undefined

    # Handle negative numbers
    if n < 0 or x < 0:
        # Check if the exponent is even or odd to get the correct sign
        if (n < 0 and x < 0):
            # Even number of negatives if exponent is even
            return False
        elif (n < 0 and x > 0):
            # Odd number of negatives if exponent is even
            return False

    # Check if x is a power of n using logarithm
    # To avoid floating point precision issues, we'll use a tolerance
    import math

    # Calculate the logarithm
    k = math.log(x, n)
    # Check if k is an integer within a small tolerance
    epsilon = 1e-10
    return abs(k - round(k)) < epsilon

    # Alternatively, use iterative multiplication to find the power
    # This avoids issues with floating point precision for very large numbers
    k = 0
    current = 1
    while current < x:
        current *= n
        k += 1
        if current == x:
            return True
    return current == x