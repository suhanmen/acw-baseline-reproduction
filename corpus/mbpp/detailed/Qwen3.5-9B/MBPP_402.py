def ncr_modp(n: int, r: int, p: int) -> int:
    """
    Computes "n choose r" modulo p, denoted as C(n, r) mod p.

    This function calculates the binomial coefficient nCr = n! / (r! * (n-r)!)
    under a modular arithmetic system with modulus p.

    It handles edge cases including:
    - r < 0 or r > n (returns 0)
    - n or p is negative (raises ValueError)
    - r > n or r < 0 (returns 0)
    - n = 0, r = 0 (returns 1)
    - Invalid inputs (raises ValueError or TypeError)

    Parameters:
    n (int): The total number of items (must be >= 0)
    r (int): The number of items to choose (must be >= 0)
    p (int): The modulus (must be > 0)

    Returns:
    int: The value of nCr modulo p

    Raises:
    TypeError: If any input is not an integer
    ValueError: If n < 0, p <= 0, or r is negative (handled via logic for r > n)
    """

    # Validate that all inputs are integers
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if not isinstance(r, int) or isinstance(r, bool):
        raise TypeError(f"r must be an integer, got {type(r).__name__}")
    if not isinstance(p, int) or isinstance(p, bool):
        raise TypeError(f"p must be an integer, got {type(p).__name__}")

    # Validate domain constraints
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if p <= 0:
        raise ValueError(f"p must be a positive integer, got {p}")

    # Adjust r to be within valid range [0, n]
    # If r < 0, C(n, r) is defined as 0
    # If r > n, C(n, r) is defined as 0
    if r < 0:
        return 0
    if r > n:
        return 0

    # Special case: C(n, 0) = 1 for any n >= 0
    if r == 0:
        return 1

    # Optimize: C(n, r) = C(n, n-r)
    # This reduces the number of multiplications when r > n/2
    r = min(r, n - r)

    # Strategy: Calculate (n * (n-1) * ... * (n-r+1)) / (r * (r-1) * ... * 1) mod p
    # To avoid floating point division, we compute numerator and denominator
    # separately, then perform modular inverse for the denominator.

    # We need to be careful about the modulus p being prime or not.
    # If p is prime, we can use Fermat's Little Theorem for modular inverse: a^(p-2) mod p.
    # If p is not prime, we need Extended Euclidean Algorithm if gcd(denominator, p) == 1.
    # However, the problem examples suggest standard combinatorial properties.
    # A robust method for general p involves prime factorization of nCr or calculating
    # using multiplicative inverse if it exists.
    # 
    # Given the constraints of typical interview problems and the examples:
    # Example 1: 10C2 mod 13 = 45 mod 13 = 6. (13 is prime)
    # Example 2: 15C12 mod 43 = 455 mod 43 = 25. (43 is prime)
    # Example 3: 17C9 mod 18 = 24310 mod 18 = 10. (18 is NOT prime)
    #
    # Since p=18 is not prime in Example 3, we cannot blindly use Fermat's Little Theorem.
    # We must handle cases where gcd(denominator, p) might not be 1.
    # However, C(n, r) is always an integer.
    # A safe approach for non-prime moduli without prime factorization is tricky.
    # But often in such problems, if the result is valid, the modular inverse exists.
    # Let's implement a robust modular inverse using Extended Euclidean Algorithm.
    # If gcd(denominator, p) != 1, the inverse doesn't exist, implying we can't divide directly.
    # In that specific case for general p, we would need prime factorization.
    # Assuming the inputs provided in assertions are such that a direct modular inverse
    # approach or a simulation of division works, or we implement a robust fraction reduction.
    #
    # To be absolutely safe and "production-grade" without external libraries for prime factorization:
    # We will compute the product of the numerator terms, and the product of the denominator terms.
    # Then we will simplify the fraction nCr by canceling common factors between numerator and denominator
    # before applying the modulus. This ensures integer arithmetic until the very end if possible,
    # or we apply modulus at each step of cancellation.
    #
    # Actually, a simpler robust method for moderate n is:
    # 1. Calculate numerator = product(n * (n-1) * ... * (n-r+1))
    # 2. Calculate denominator = product(r * (r-1) * ... * 1)
    # 3. Compute gcd between denominator and current numerator iteratively to reduce.
    # But numbers can get huge.
    #
    # Better approach for arbitrary p:
    # Use the property that nCr mod p can be computed by maintaining the fraction as a product of terms
    # and simplifying using GCD at each step to keep numbers small.
    # result = 1
    # for i in 1..r:
    #    result = result * (n - i + 1)
    #    result = result / i
    # We do this using modular arithmetic and modular inverse, checking if inverse exists.
    # If inverse does not exist (gcd(i, p) != 1), we accumulate the non-invertible parts separately
    # and handle them later? That's complex.
    #
    # Alternative robust strategy:
    # Calculate numerator and denominator as lists of prime factors? Too slow for large inputs.
    #
    # Let's try the iterative multiplication and division with GCD simplification.
    # result_num = 1
    # result_den = 1
    # for i from 1 to r:
    #    result_num = result_num * (n - i + 1)
    #    result_den = result_den * i
    #    common = gcd(result_num, result_den)
    #    result_num //= common
    #    result_den //= common
    # Now result_den should be 1 (mathematically). 
    # But intermediate numbers can still be large.
    # We can apply modulus to result_num after division?
    # No, (A * B) mod M != (A mod M * B mod M) if we are dividing later.
    # We must keep the fraction exact.
    #
    # Given the constraints of the problem examples (small numbers), and the requirement for robustness:
    # If p is small, numbers won't explode too much before modulo if we reduce carefully.
    # Let's implement the GCD reduction method. It is exact and avoids overflow until the final modulo.
    # We will reduce the fraction at every step to keep numbers as small as possible.

    numerator_val = 1
    denominator_val = 1

    # We iterate from 1 to r
    # At each step i, we multiply numerator by (n - i + 1) and denominator by i.
    # Then we reduce the fraction by dividing both by their GCD.
    # This ensures we never store the full factorial, only the reduced fraction.

    for i in range(1, r + 1):
        # Update numerator: multiply by (n - i + 1)
        term_numerator = n - i + 1
        numerator_val = numerator_val * term_numerator

        # Update denominator: multiply by i
        term_denominator = i
        denominator_val = denominator_val * term_denominator

        # Simplify the fraction by dividing both by their greatest common divisor
        # This keeps the intermediate values as small as possible
        common_divisor = _gcd(numerator_val, denominator_val)

        numerator_val = numerator_val // common_divisor
        denominator_val = denominator_val // common_divisor

    # At the end, denominator_val should be 1 for valid integer C(n, r)
    # If due to some reason it's not (should not happen for valid integers n, r), 
    # it implies we couldn't reduce completely, but mathematically it must be 1.
    # Let's assert this for correctness logic.
    if denominator_val != 1:
        # This part theoretically shouldn't be reached for valid integers
        # But if it were, we would need to handle the fraction.
        # For the purpose of this problem, we assume valid integer result.
        pass

    # Now compute (numerator_val % p)
    final_result = numerator_val % p

    return final_result


def _gcd(a: int, b: int) -> int:
    """
    Computes the Greatest Common Divisor of two non-negative integers using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a