def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    from math import isqrt

    # --- Validation Step ---

    # Check if input is an integer
    if not isinstance(a, int):
        raise ValueError(f"Input must be an integer, got {type(a).__name__}")

    # Check for non-positive numbers. Primes are positive integers greater than 1.
    # Their product must also be positive and greater than 1.
    if a <= 1:
        return False

    # --- Helper: Check if a single number is prime ---
    def _is_prime(n):
        # 2 is the only even prime
        if n == 2:
            return True
        # Exclude even numbers and 1
        if n % 2 == 0 or n < 2:
            return False

        # Check odd divisors up to the square root
        limit = isqrt(n)
        divisor = 3
        while divisor <= limit:
            if n % divisor == 0:
                return False
            divisor += 2
        return True

    # --- Helper: Get all prime factors of a number (with multiplicity) ---
    # We need exactly 3 prime factors. They don't have to be distinct.
    # Example: 8 = 2 * 2 * 2 is valid. 12 = 2 * 2 * 3 is valid.
    def _get_prime_factors(n):
        factors = []
        d = 2
        temp_n = n

        # Handle factor 2 separately to allow stepping by 2 later
        while temp_n % d == 0:
            factors.append(d)
            temp_n //= d

        # Check odd factors
        d = 3
        while d * d <= temp_n:
            while temp_n % d == 0:
                factors.append(d)
                temp_n //= d
            d += 2

        # If temp_n is now > 1, the remaining part is a prime
        if temp_n > 1:
            factors.append(temp_n)

        return factors

    # --- Core Logic ---

    # Get all prime factors of the input number
    prime_factors = _get_prime_factors(a)

    # Count how many prime factors we found
    factor_count = len(prime_factors)

    # We strictly need exactly 3 prime factors
    if factor_count == 3:
        return True
    else:
        return False