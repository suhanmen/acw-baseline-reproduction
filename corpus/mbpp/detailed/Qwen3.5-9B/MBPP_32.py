def is_prime_candidate(number: int) -> bool:
    """
    Check if a number is potentially prime by verifying it is greater than 1
    and not divisible by any integer from 2 up to its square root.

    This function handles the core primality test required for factorization.
    It returns True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    # We only need to check odd divisors up to the square root of the number
    limit = int(number ** 0.5) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False

    return True


def get_prime_factors(n: int) -> list[int]:
    """
    Generate a list of all prime factors of n, including duplicates.

    Strategy:
    1. Handle the factor 2 separately to allow us to skip even numbers later.
    2. Iterate through odd numbers starting from 3.
    3. While the current divisor divides n, add it to the list and divide n.
    4. Continue until n becomes 1 or the divisor exceeds the square root of n.
    5. If n is greater than 1 after the loop, the remaining n is a prime factor itself.

    This approach is efficient and explicitly spells out each step.
    """
    factors = []

    # Handle negative inputs by converting to absolute value for factorization logic
    # while preserving the understanding that prime factors are defined for positive integers.
    n = abs(n)

    if n == 0:
        # 0 has infinite prime factors or is undefined depending on context,
        # but mathematically it is not a candidate for having a "largest" prime factor in a standard sense.
        # We return an empty list to indicate no valid prime factors exist for 0.
        return factors

    if n == 1:
        # 1 has no prime factors.
        return factors

    # Step 1: Extract all factors of 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Step 2: Extract odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 2

    # Step 3: If n > 1, the remaining number is a prime factor
    if n > 1:
        factors.append(n)

    return factors


def max_Prime_Factors(n: int) -> int:
    """
    Find the largest prime factor of a given number n.

    This function:
    1. Validates the input (must be an integer).
    2. Handles edge cases (0, 1, negative numbers).
    3. Calculates all prime factors.
    4. Returns the maximum among them.

    Asserts:
    max_Prime_Factors(15) == 5
    max_Prime_Factors(6) == 3
    max_Prime_Factors(2) == 2
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Edge Case: Zero
    if n == 0:
        raise ValueError("Cannot find prime factors for zero.")

    # Edge Case: One
    if n == 1:
        raise ValueError("One does not have any prime factors.")

    # Handle negative numbers by taking the absolute value
    # Prime factorization is defined on the magnitude of the integer.
    # Example: -15 has prime factors 3 and 5.
    absolute_n = abs(n)

    if absolute_n == 1:
        raise ValueError("After taking absolute value, 1 does not have any prime factors.")

    # Get the list of all prime factors
    prime_factors_list = get_prime_factors(absolute_n)

    # If the list is empty (should theoretically not happen with the checks above for n != 0, 1),
    # handle it safely to avoid runtime errors.
    if len(prime_factors_list) == 0:
        raise ValueError("No prime factors found.")

    # Find the maximum value in the list
    largest_factor = 0
    for factor in prime_factors_list:
        if factor > largest_factor:
            largest_factor = factor

    return largest_factor