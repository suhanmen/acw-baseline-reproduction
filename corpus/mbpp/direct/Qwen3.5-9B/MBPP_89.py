def closest_num(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be greater than 0.")
    return n - 1