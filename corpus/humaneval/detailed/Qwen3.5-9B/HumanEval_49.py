def modp(n: int, p: int):
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

    def validate_input(x: int, name: str) -> None:
        """Ensure the input is a valid non-negative integer and raise TypeError otherwise."""
        if not isinstance(x, int):
            raise TypeError(f"{name} must be an integer, got {type(x).__name__}")
        if isinstance(x, bool):
            raise TypeError(f"{name} must be an integer, got {type(x).__name__} (bool is a subclass of int but not allowed here)")
        if x < 0:
            raise ValueError(f"{name} must be non-negative, got {x}")

    def validate_modulus(p_val: int, name: str) -> None:
        """Ensure the modulus is a valid positive integer greater than 0."""
        validate_input(p_val, name)
        if p_val <= 0:
            raise ValueError(f"{name} must be strictly positive, got {p_val}")

    def modular_exponentiation(base: int, exp: int, modulus: int) -> int:
        """
        Calculate (base ** exp) % modulus using binary exponentiation (square-and-multiply).
        This approach is O(log exp) and avoids computing the full power, preventing
        memory overflow and excessive CPU time for large exponents.
        """
        # Ensure base is reduced modulo m at the start to handle any base >= m
        result = 1
        current_base = base % modulus

        # If the modulus is 1, any number modulo 1 is 0. 
        # However, we expect p > 0 from validation. If p=1, result is always 0.
        # Note: 2^0 % 1 = 1 % 1 = 0. The formula holds.
        if modulus == 1:
            return 0

        while exp > 0:
            # If the current exponent bit is 1, multiply the result by the current base
            if exp % 2 == 1:
                result = (result * current_base) % modulus

            # Square the base for the next bit position
            current_base = (current_base * current_base) % modulus

            # Shift the exponent to the right (divide by 2)
            exp = exp // 2

        return result

    # Step 1: Validate the exponent 'n'
    validate_input(n, "n")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Step 2: Validate the modulus 'p'
    validate_input(p, "p")
    if p <= 0:
        raise ValueError("p must be strictly positive")

    # Step 3: Compute 2^n mod p using the helper function
    final_result = modular_exponentiation(2, n, p)

    return final_result