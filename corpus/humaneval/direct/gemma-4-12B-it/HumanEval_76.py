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
    # Special case: if n is 1, x must be 1 (1^any_int = 1)
    if n == 1:
        return x == 1

    # If n is 0, x can only be 1 (0^0) or 0 (0^k where k > 0)
    # However, standard definition of "simple power" usually implies positive integers or 
    # specific behavior. Looking at examples: 1 is a power of 4 (4^0).
    if n == 0:
        return x == 0 or x == 1

    # For n > 1, we check if x is n^k for some non-negative integer k
    # Since x = n^k, x must be positive (unless n is negative, but examples suggest n > 1)
    if x < 0:
        return False

    # Start from k=0 (n^0 = 1)
    current = 1
    while current <= x:
        if current == x:
            return True
        current *= n
        # Safety break to prevent infinite loop if n=1 or n=0 (handled above)
        if n <= 1 and current == x:
            break

    return False