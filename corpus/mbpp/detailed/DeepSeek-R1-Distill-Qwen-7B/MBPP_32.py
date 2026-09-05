def max_Prime_Factors(n):
    # Validate the input to be a positive integer greater than 1
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n <= 1:
        raise ValueError("Input must be greater than 1.")

    # Handle the case where n is 2
    if n == 2:
        return 2

    largest_prime = -1

    # Divide out all factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2

    # Now n must be odd. Start from 3, increment by 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i += 2

    # If remaining n is a prime number greater than 2
    if n > 2:
        largest_prime = n

    return largest_prime