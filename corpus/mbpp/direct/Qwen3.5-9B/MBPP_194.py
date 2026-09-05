def octal_To_Decimal(n: int) -> int:
    """Convert an octal number represented as an integer to its decimal equivalent."""
    if n < 0:
        raise ValueError("Octal number must be non-negative.")

    decimal_value = 0
    power = 1

    while n > 0:
        digit = n % 10
        decimal_value += digit * power
        n //= 10
        power *= 8

    return decimal_value