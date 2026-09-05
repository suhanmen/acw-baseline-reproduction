def babylonian_squareroot(n):
    """
    Computes the square root of a number n using the Babylonian method 
    (also known as Heron's method).
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0:
        return 0.0

    # Initial guess
    x = n / 2.0
    # Tolerance for floating point precision
    tolerance = 1e-15

    while True:
        better_guess = (x + n / x) / 2.0
        if abs(x - better_guess) < tolerance:
            return better_guess
        x = better_guess

if __name__ == "__main__":
    assert babylonian_squareroot(10) == 3.162277660168379
    assert babylonian_squareroot(2) == 1.414213562373095
    assert babylonian_squareroot(9) == 3.0