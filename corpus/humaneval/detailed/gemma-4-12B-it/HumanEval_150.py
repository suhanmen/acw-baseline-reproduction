import math

def is_prime(number: int) -> bool:
    """
    Determines if a given integer is a prime number.

    A prime number is a natural number greater than 1 that has 
    no positive divisors other than 1 and itself.
    """
    # Prime numbers must be integers.
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, received {type(number).__name__}")

    # Handle numbers less than 2 (0, 1, and negative numbers are not prime).
    if number < 2:
        return False

    # 2 is the only even prime number.
    if number == 2:
        return True

    # Eliminate all other even numbers immediately.
    if number % 2 == 0:
        return False

    # Check for factors from 3 up to the square root of the number.
    # We only need to check odd numbers.
    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False

    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    x_or_y(7, 34, 12) == 34
    x_or_y(15, 8, 5) == 5

    """
    # Validation: Ensure n is an integer to perform primality test.
    # We allow x and y to be any type as the problem doesn't restrict their values.
    if not isinstance(n, int):
        raise TypeError("The first argument 'n' must be an integer.")

    # Step 1: Determine if n is a prime number.
    is_n_prime = is_prime(n)

    # Step 2: Determine the result based on the primality of n.
    if is_n_prime:
        # If n is prime, the result is x.
        result = x
    else:
        # If n is not prime, the result is y.
        result = y

    # Step 3: Return the final determined value.
    return result