def dif_Square(n):
    if n < 0:
        return False  # Since n is positive, difference of squares can't be negative
    # Handle edge cases
    if n == 0:
        return True  # 0 = 0^2 - 0^2
    if n == 1:
        return True  # 1 = 1^2 - 0^2

    # Find all factor pairs (x, y) such that x * y = n and y >= x
    max_factor = int(n ** 0.5)
    for x in range(1, max_factor + 1):
        if n % x == 0:
            y = n // x
            # Check if x and y have the same parity
            if (x % 2 == y % 2):
                return True
    return False