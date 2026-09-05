def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5

    """
    def _is_prime_check(number: int) -> bool:
        """
        Helper function to determine if a number is prime.

        Logic:
        1. Numbers <= 1 are not prime.
        2. 2 and 3 are prime.
        3. Eliminate multiples of 2 and 3.
        4. Check divisibility by numbers of form 6k ± 1 up to sqrt(n).
        """
        # Handle small numbers explicitly
        if number <= 1:
            return False

        if number <= 3:
            return True

        if number % 2 == 0 or number % 3 == 0:
            return False

        # Check for factors up to the square root of the number
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6

        return True

    # Validate input types explicitly
    if not isinstance(n, int):
        raise TypeError(f"The first argument 'n' must be an integer, got {type(n).__name__}")

    if not isinstance(x, int):
        raise TypeError(f"The second argument 'x' must be an integer, got {type(x).__name__}")

    if not isinstance(y, int):
        raise TypeError(f"The third argument 'y' must be an integer, got {type(y).__name__}")

    # Determine primality of n
    is_n_prime = _is_prime_check(n)

    # Return x if n is prime, otherwise return y
    if is_n_prime:
        return x
    else:
        return y