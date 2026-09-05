def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. """

    # Check if the input is an integer
    if not isinstance(a, int):
        return False

    # Check if the number is positive
    if a <= 0:
        return False

    # Function to factorize a number into its prime factors
    def factorize(n):
        factors = []
        # Divide by 2 until n is odd
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        # Now check odd numbers from 3 up to sqrt(n)
        i = 3
        max_factor = (n ** 0.5)
        while i <= max_factor:
            while n % i == 0:
                factors.append(i)
                n = n // i
                max_factor = (n ** 0.5)
            i += 2
        # If remaining n is a prime greater than 2
        if n > 2:
            factors.append(n)
        return factors

    # Get the prime factors of 'a'
    prime_factors = factorize(a)

    # Check if there are exactly three prime factors (including duplicates)
    if len(prime_factors) == 3:
        return True
    else:
        return False