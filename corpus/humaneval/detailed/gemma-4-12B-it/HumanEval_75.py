import math

def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.
    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.
    """
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to the square root of n
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Input validation for data type
    if not isinstance(a, int):
        return False

    # Problem context: a is less than 100.
    # Technically, for a number to be a product of 3 primes, 
    # the smallest possible value is 2 * 2 * 2 = 8.
    if a < 8 or a >= 100:
        return False

    # We need to find if a = p1 * p2 * p3 where p1, p2, p3 are primes.
    # Since a < 100, we can iterate through possible prime factors.
    # We use a list to store the factors we find.
    factors = []
    temp_val = a

    # We iterate starting from the smallest prime, 2.
    # Since a < 100, we don't need to check very high.
    for i in range(2, 100):
        # If i is a factor of the current temp_val
        if temp_val % i == 0:
            # Check if the factor i is a prime number
            if is_prime(i):
                factors.append(i)
                # Divide temp_val by this factor as many times as it goes in
                # However, the problem asks for a product of EXACTLY 3 primes.
                # If a = 8 (2*2*2), we need to account for all three.
                while temp_val % i == 0:
                    temp_val //= i
                    # Note: We only want to add to factors list if it's a factor
                    # in the prime factorization. The logic below ensures we count 
                    # how many prime factors exist in total.
                    # Let's refactor the logic slightly for clarity:
                    pass

    # Refined logic for counting prime factors:
    # We need to find the prime factorization of 'a' and see if 
    # the count of factors (counting multiplicities) is exactly 3.

    final_factors = []
    remaining_n = a

    # Trial division for prime factorization
    divisor = 2
    while divisor * divisor <= remaining_n:
        while remaining_n % divisor == 0:
            final_factors.append(divisor)
            remaining_n //= divisor
        divisor += 1

    # If remaining_n > 1, the remaining part is a prime factor
    if remaining_n > 1:
        final_factors.append(remaining_n)

    # The problem asks if the number is the product of 3 primes.
    # This means the count of the prime factors in the factorization must be exactly 3.
    # Example: 30 = 2 * 3 * 5 (3 factors) -> True
    # Example: 8 = 2 * 2 * 2 (3 factors) -> True
    # Example: 12 = 2 * 2 * 3 (3 factors) -> True
    # Example: 4 = 2 * 2 (2 factors) -> False
    # Example: 70 = 2 * 5 * 7 (3 factors) -> True

    factor_count = len(final_factors)

    if factor_count == 3:
        return True
    else:
        return False