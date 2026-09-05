def get_Min_Squares(n):
    # First, handle negative input by returning -1
    if n < 0:
        return -1

    # Check if n is zero (though the problem says n is positive, handle just in case)
    if n == 0:
        return 0

    # Check for perfect square
    sqrt_n = int(n ** 0.5)
    if sqrt_n * sqrt_n == n:
        return 1

    # Check for sum of two squares
    for a in range(sqrt_n, -1, -1):
        b_squared = n - a * a
        if b_squared < 0:
            continue
        b = int(b_squared ** 0.5)
        if b * b == b_squared:
            return 2

    # If none of the above, return 4 as per mathematical theorem
    return 4