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
    if x < 1:
        return False
    if n < 0 or n == 0 or n == 1:
        if n == 0 and x == 1:
            return True
        if n == 1 and x == 1:
            return True
        return False
    while x > 1:
        if x % n != 0:
            return False
        x //= n
    return x == 1