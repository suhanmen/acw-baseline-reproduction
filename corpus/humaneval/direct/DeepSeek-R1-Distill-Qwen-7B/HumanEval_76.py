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
    if n == 0:
        return x == 0
    if x == 0:
        return False  # Because 0 cannot be expressed as n^k for n != 0
    if n == 1:
        return x == 1
    k = 0
    while True:
        current = n ** k
        if current == x:
            return True
        if current > x:
            return False
        k += 1
        if k > abs(x):  # Prevent infinite loop in case of overflow
            return False