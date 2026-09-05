def multiply_int(a: int, b: int) -> int:
    """
    Multiplies two integers without using the * operator.
    """
    # Handle signs
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)

    result = 0
    # Use repeated addition
    # Optimization: iterate over the smaller number
    if a < b:
        a, b = b, a

    for _ in range(b):
        result += a

    return -result if negative else result

if __name__ == "__main__":
    assert multiply_int(10, 20) == 200
    assert multiply_int(5, 10) == 50
    assert multiply_int(4, 8) == 32