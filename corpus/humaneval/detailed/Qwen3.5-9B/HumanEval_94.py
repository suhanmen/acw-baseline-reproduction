def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    # --- Helper Function 1: Validate the input list ---
    # Ensure the input is a list and contains only integers.
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    validated_integers = []
    for item in lst:
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers, got {type(item).__name__} instead.")
        # Explicitly handle boolean values as they are technically integers in Python (True/False == 1/0)
        if isinstance(item, bool):
            raise TypeError("Boolean values are not allowed in the list.")
        # Handle negative numbers based on problem context (primes are positive)
        # We will collect them but filter them out during prime checking.
        validated_integers.append(item)

    # --- Helper Function 2: Check if a number is prime ---
    # Primes are defined as integers greater than 1 with exactly two factors.
    def is_prime(n):
        # Negative numbers, zero, and one are not prime
        if n < 2:
            return False

        # 2 is prime
        if n == 2:
            return True

        # All other even numbers are not prime
        if n % 2 == 0:
            return False

        # Check for factors from 3 up to the square root of n
        # We only need to check odd numbers up to sqrt(n)
        import math
        limit = int(math.isqrt(n))

        for divisor in range(3, limit + 1, 2):
            if n % divisor == 0:
                return False

        return True

    # --- Helper Function 3: Calculate the sum of digits of a non-negative integer ---
    # Since we filter for primes (which are positive), the number will be > 0.
    def sum_of_digits(num):
        # Convert number to string, iterate characters, convert back to int, and sum.
        # Alternative purely arithmetic approach:
        total = 0
        current_num = abs(num) # Ensure positive just in case, though logic guarantees it
        while current_num > 0:
            digit = current_num % 10
            total += digit
            current_num = current_num // 10
        return total

    # --- Main Logic ---

    # 1. Filter the validated list to keep only prime numbers.
    prime_numbers = []
    for number in validated_integers:
        if is_prime(number):
            prime_numbers.append(number)

    # 2. Check if any prime was found.
    if not prime_numbers:
        # If no primes exist, we cannot find the largest one.
        # Based on typical problem constraints, we might return None or 0.
        # Given the examples all imply a result, and no case has no primes,
        # returning None is the safest explicit signal of an impossible state.
        return None

    # 3. Find the largest prime value.
    # Since the list might be unsorted, we find the maximum explicitly.
    largest_prime = max(prime_numbers)

    # 4. Calculate the sum of the digits of the largest prime.
    result = sum_of_digits(largest_prime)

    return result