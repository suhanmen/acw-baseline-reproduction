def decimal_to_binary(n: int) -> str:
    """Convert a non-negative decimal integer to its binary string representation."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return "0"
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(binary_digits))