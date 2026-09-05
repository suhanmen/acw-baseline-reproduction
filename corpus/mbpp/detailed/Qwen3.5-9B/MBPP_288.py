from typing import List, Optional

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Computes the Extended Greatest Common Divisor (EGCD) for two integers a and b.

    Returns a tuple (g, x, y) such that:
      a*x + b*y = g
    where g is the greatest common divisor of a and b.

    This is implemented iteratively to avoid recursion depth issues and for clarity.
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # At the end of the loop:
    # old_r contains the gcd (g)
    # old_s and old_t are the Bezout coefficients (x and y)
    return old_r, old_s, old_t


def modular_inverse_exists(n: int, p: int) -> bool:
    """
    Determines if the modular inverse of n exists modulo p.

    The modular inverse exists if and only if gcd(n, p) == 1.
    Since p is required to be a prime number, this is true as long as n is not
    a multiple of p.

    Args:
        n: The integer for which we want to find the inverse.
        p: The prime modulus.

    Returns:
        True if an inverse exists, False otherwise.
    """
    if p <= 0:
        return False
    if n == 0:
        return False  # gcd(0, p) = p != 1 (unless p=1 which is not prime, or p=0)

    # We calculate gcd(n, p). If p is prime, gcd(n, p) is 1 unless n is a multiple of p.
    # However, we use the general gcd check via extended_gcd to be robust.
    _, gcd_val, _ = extended_gcd(n, p)
    return gcd_val == 1


def compute_modular_inverse(n: int, p: int) -> int:
    """
    Computes the modular inverse of n modulo p.

    If the inverse does not exist (i.e., gcd(n, p) != 1), it raises a ValueError.

    Args:
        n: The integer to invert.
        p: The prime modulus.

    Returns:
        The modular inverse of n modulo p.
    """
    if p <= 1:
        raise ValueError(f"Modulus p must be greater than 1, got {p}")

    if n % p == 0:
        raise ValueError(f"Modular inverse does not exist for {n} modulo {p} as they are not coprime")

    g, x, _ = extended_gcd(n, p)

    if g != 1:
        raise ValueError(f"Modular inverse does not exist for {n} modulo {p}")

    # The result from extended_gcd can be negative, so we normalize it to be in [0, p-1]
    return x % p


def count_elements_with_self_inverse(elements: List[int], modulus: int, prime: int) -> int:
    """
    Counts the number of elements in the list `elements` such that their modular
    inverse under the given prime `prime` is equal to the element itself.

    An element `x` has a modular inverse equal to itself if:
      x * x ≡ 1 (mod p)
      AND x must have a valid modular inverse (i.e., gcd(x, p) == 1).

    This condition implies that x^2 - 1 ≡ 0 (mod p), or (x - 1)(x + 1) ≡ 0 (mod p).
    Since p is prime, this generally holds for x ≡ 1 or x ≡ -1 (mod p).
    However, we will perform the check explicitly using the modular inverse function
    to satisfy the requirement of validating inputs and handling edge cases robustly,
    rather than relying solely on the mathematical derivation which might have edge cases
    regarding the definition of the inverse itself in the context of the problem statement.

    Specifically, we verify:
    1. Does the element have a modular inverse?
    2. If yes, is (element * inverse) % prime == 1? (Standard check)
    3. Is the inverse value exactly equal to the element value?

    The problem statement asks for "modular inverse ... equal to itself".
    So we must explicitly calculate inv = modInverse(x, p) and check if inv == x.

    Args:
        elements: A list of integers to be checked.
        modulus: An integer parameter (currently unused in logic but part of signature).
        prime: The prime number p under which the modular arithmetic is performed.

    Returns:
        The count of elements satisfying the condition.

    Raises:
        ValueError: If prime is not a prime number or if prime <= 1.
                    If elements contains non-integer types (handled by type hinting).
    """

    # --- Input Validation Phase ---

    # Validate 'prime'
    if not isinstance(prime, int):
        raise TypeError("The 'prime' argument must be an integer.")
    if prime <= 1:
        raise ValueError("The 'prime' argument must be a positive integer greater than 1.")
    # Note: The problem states 'prime' is given as a prime number.
    # A strict primality test could be added here, but typically in such problems,
    # the assumption is that the input is valid per the description.
    # However, for "defensive coding", we might check if it's actually prime.
    # Let's implement a simple primality check to be thorough.
    is_prime = True
    if prime < 2:
        is_prime = False
    else:
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                is_prime = False
                break

    if not is_prime:
        raise ValueError("The provided number is not a prime number.")

    # Validate 'modulus' (as per signature, though logic relies on 'prime')
    # The problem description implies 'modulus' and 'prime' might be synonymous or 
    # 'modulus' is just the context. We will trust 'prime' for the math.
    # We'll ensure modulus is an integer too.
    if not isinstance(modulus, int):
        raise TypeError("The 'modulus' argument must be an integer.")

    # Validate 'elements'
    if not isinstance(elements, list):
        raise TypeError("The 'elements' argument must be a list.")

    # Iterate and count
    count = 0

    # Handle empty list explicitly
    if len(elements) == 0:
        return count

    for element in elements:
        # Check type of element
        if not isinstance(element, int):
            # Strictly speaking, math doesn't work on floats for modular inverse in integers.
            # If floats are passed, we should probably reject or round. Given "production-grade",
            # rejecting non-integers is safer for modular arithmetic.
            raise TypeError(f"All elements in the list must be integers. Found {type(element)}")

        # Check for negative numbers? Modular arithmetic handles negatives.
        # But let's ensure the value is treated correctly. Python's % handles negatives well.
        # e.g., -1 % 7 == 6. 
        # Does -1 have inverse equal to -1? (-1 * -1) % 7 = 1. Yes.
        # So negative numbers are valid inputs.

        # Step 1: Check if element is 0
        # 0 does not have a modular inverse unless modulus is 1 (which we already checked > 1).
        if element == 0:
            # 0 * x = 0 != 1 mod p for any p > 1. So inverse doesn't exist.
            continue

        # Step 2: Check if element is a multiple of prime
        # If element % prime == 0, then gcd(element, prime) = prime != 1.
        # extended_gcd or modular_inverse_exists handles this, but we can skip early.
        if element % prime == 0:
            continue

        # Step 3: Compute the modular inverse
        try:
            inverse = compute_modular_inverse(element, prime)
        except ValueError:
            # This catches cases where gcd != 1, though we filtered multiples above.
            # Keep the try-except for robustness in the general helper.
            continue

        # Step 4: Verify the condition: inverse == element
        # The problem asks for "modular inverse ... equal to itself".
        if inverse == element:
            count += 1

    return count