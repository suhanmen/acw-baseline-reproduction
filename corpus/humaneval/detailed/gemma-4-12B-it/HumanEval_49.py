def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Input Validation: Ensure types are integers
    if not isinstance(n, int) or not isinstance(p, int):
        raise TypeError("Both 'n' and 'p' must be integers.")

    # Handle edge case for p <= 0: Modulo by zero or negative is mathematically 
    # undefined or specific to convention. Standard modular arithmetic expects p > 0.
    if p <= 0:
        raise ValueError("The modulus 'p' must be a positive integer.")

    # Handle the base case for n < 0:
    # Modular exponentiation for negative exponents requires the modular 
    # multiplicative inverse. However, the problem description implies 
    # standard positive integer exponentiation (2^n). 
    # If n is negative, we handle it by treating it as an error or 
    # standard power rules, but given the context of "modp" (modular power),
    # we check for negative n to prevent infinite loops or complex results.
    if n < 0:
        raise ValueError("The exponent 'n' must be a non-negative integer.")

    # Handle the base case for p = 1:
    # Any integer modulo 1 is 0.
    if p == 1:
        return 0

    # Handle the base case for n = 0:
    # 2^0 is always 1. 1 modulo p is 1 (unless p=1, handled above).
    if n == 0:
        return 1 % p

    # To avoid overflow and ensure performance, we use the Modular Exponentiation 
    # algorithm (Binary Exponentiation / Square-and-Multiply).
    # This ensures the result stays within [0, p-1] at each step.

    def power_modulo(base: int, exponent: int, modulus: int) -> int:
        """Helper to perform (base^exponent) % modulus efficiently."""
        result = 1
        base = base % modulus

        while exponent > 0:
            # If exponent is odd, multiply result by the current base
            if exponent % 2 == 1:
                result = (result * base) % modulus

            # Square the base and halve the exponent
            base = (base * base) % modulus
            exponent = exponent // 2

        return result

    # Execute the modular exponentiation
    # We want (2^n) % p
    final_result = power_modulo(2, n, p)

    return final_result