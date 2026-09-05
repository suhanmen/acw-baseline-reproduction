def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Check if the input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    # Check if the integer is a positive number
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    # Precompute factorials from 1 to n
    factorials = []
    for i in range(1, n+1):
        # Compute the factorial of i
        factorial_i = 1
        for j in range(1, i+1):
            factorial_i *= j
        factorials.append(factorial_i)

    # Multiply all factorials together
    product = 1
    for fact in factorials:
        product *= fact

    return product