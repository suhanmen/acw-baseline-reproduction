from math import isqrt


def _is_prime_candidate(number: int) -> bool:
    """
    Determines if a given number is a prime number.

    This function handles edge cases:
    - Numbers less than or equal to 1 are not prime.
    - 2 and 3 are prime.
    - Even numbers greater than 2 are not prime.
    - Numbers divisible by 3 greater than 3 are not prime.
    - For larger numbers, it checks divisibility by factors up to the square root.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def _generate_fibonacci_sequence(count_needed: int) -> list[int]:
    """
    Generates Fibonacci numbers until enough prime Fibonacci numbers are found.

    The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    Note: We start checking from the first few Fibonacci numbers manually 
    to handle the 0 and 1 cases correctly, then generate the rest.

    Args:
        count_needed (int): The total number of prime Fibonacci numbers required.

    Returns:
        list[int]: A list containing the first 'count_needed' prime Fibonacci numbers.
    """
    if count_needed < 1:
        return []

    # Known prime Fibonacci numbers: 2, 3, 5, 13, 89, 233, 1597, 28657, 514229, ...
    # We will generate them on the fly.

    # Initialize the first two Fibonacci numbers
    fib_a = 0
    fib_b = 1

    prime_fibs = []
    current_index = 0

    # We need to find at least 'count_needed' prime Fibonacci numbers.
    # To avoid infinite loops in case of logic errors, we set a reasonable upper bound on iterations.
    # However, mathematically, we assume we can always find more prime Fibonacci numbers.
    max_iterations = 100000  # Safety limit, though unlikely to be reached for small n

    while len(prime_fibs) < count_needed and current_index < max_iterations:
        # Check the current Fibonacci number (fib_a)
        if fib_a > 1 and _is_prime_candidate(fib_a):
            prime_fibs.append(fib_a)

        # Generate the next Fibonacci number
        next_fib = fib_a + fib_b
        fib_a = fib_b
        fib_b = next_fib

        current_index += 1

        # If we've iterated too much without finding enough, break to avoid infinite loops
        if current_index >= max_iterations:
            break

    return prime_fibs


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    The sequence of prime Fibonacci numbers starts: 2, 3, 5, 13, 89, ...
    Indexing is 1-based as per the docstring examples.

    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Validate input type
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    # Validate input value
    if n < 1:
        raise ValueError("Input 'n' must be a positive integer greater than or equal to 1.")

    # Generate the sequence of prime Fibonacci numbers
    sequence = _generate_fibonacci_sequence(n)

    # Return the n-th element (since we generated exactly n elements)
    # If sequence length is somehow less than n (shouldn't happen with current logic), raise error
    if len(sequence) < n:
        raise RuntimeError(f"Could not generate {n} prime Fibonacci numbers. Sequence ended prematurely with {len(sequence)} items.")

    return sequence[n - 1]