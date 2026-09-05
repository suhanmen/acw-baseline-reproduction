def _is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division.

    Rules:
    - Numbers less than 2 are not prime.
    - 2 is prime.
    - Even numbers greater than 2 are not prime.
    - Odd numbers are checked up to sqrt(n).
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n ** 0.5) + 1
    for candidate in range(3, limit, 2):
        if n % candidate == 0:
            return False
    return True


def _prime_factors(value: int) -> dict:
    """
    Decompose a positive integer into its prime factorization.

    Returns a dictionary mapping each prime factor to its exponent (count).
    Raises ValueError if the input is not a positive integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected an integer, got {type(value).__name__}")

    if value <= 0:
        raise ValueError(f"Expected a positive integer (>= 1), got {value}")

    factors = {}
    n = value

    # Handle factor of 2 separately to optimize the loop for odd numbers
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

    # Check for odd factors starting from 3
    factor_candidate = 3
    while factor_candidate * factor_candidate <= n:
        while n % factor_candidate == 0:
            factors[factor_candidate] = factors.get(factor_candidate, 0) + 1
            n //= factor_candidate
        factor_candidate += 2

    # If n is still greater than 1, then the remaining n is a prime
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def _get_next_multiple(n: int, step: int) -> int:
    """
    Calculate the smallest number >= n that is divisible by step.

    Logic:
    - If n is already divisible by step, return n.
    - Otherwise, return the next multiple.
    """
    if step <= 0:
        raise ValueError("Step must be a positive integer.")

    remainder = n % step
    if remainder == 0:
        return n
    else:
        return n + (step - remainder)


def first_Factorial_Divisible_Number(x: int) -> int:
    """
    Find the first natural number n such that n! (n factorial) is divisible by x.

    Strategy:
    1. Validate input x.
    2. Factorize x into prime factors with their counts.
    3. For each prime factor p with count c, find the smallest n such that
       n! contains at least c instances of p.
    4. The answer is the maximum of these n values across all prime factors.

    Edge cases handled:
    - x = 1: Returns 1 (1! = 1, divisible by 1).
    - Single element, zero, negative: Raises ValueError.
    - Non-integer inputs: Raises TypeError.
    """
    # Input Validation
    if not isinstance(x, int):
        raise TypeError(f"Input must be an integer, received: {type(x).__name__}")

    if x <= 0:
        raise ValueError(f"Input must be a positive integer (>= 1), received: {x}")

    # Special case: 0! = 1 and 1! = 1. Both are divisible by 1.
    # The problem asks for the "first" natural number.
    # Since 1 is the first natural number and 1! is divisible by 1, return 1.
    if x == 1:
        return 1

    # Step 1: Get prime factorization of x
    # Example: x = 10 -> {2: 1, 5: 1}
    # Example: x = 5 -> {5: 1}
    prime_counts = _prime_factors(x)

    max_n = 0

    # Step 2: For each prime factor, find the minimal n satisfying the condition
    for prime, required_count in prime_counts.items():
        current_n = 0

        # We search linearly for n because the numbers are generally small enough
        # for factorials to grow very quickly. 
        # LeetCode constraint usually keeps x within range where n < 100.
        # We simulate counting factors in factorial(n) until we reach required_count.

        n = 0
        while True:
            n += 1
            count_in_factorial = 0

            # Count how many times 'prime' appears in n!
            # Legendre's Formula: sum(floor(n / p^k)) for k >= 1
            temp_n = n
            temp_prime = prime

            # Simple iterative counting for clarity and robustness
            divisor = prime
            while divisor <= temp_n:
                count_in_factorial += temp_n // divisor
                # Prevent potential overflow or infinite loop if divisor doesn't grow
                # though mathematically it will grow since prime >= 2
                try:
                    divisor *= prime
                except OverflowError:
                    # In Python integers have arbitrary precision, but this handles logic safety
                    break

            if count_in_factorial >= required_count:
                # This n is sufficient for this specific prime factor
                if n > max_n:
                    max_n = n
                break

        # Update max_n to ensure all prime constraints are met
        # (Though in this loop structure, we break immediately once found, 
        # we compare against running max_n to find the global bottleneck)

    return max_n