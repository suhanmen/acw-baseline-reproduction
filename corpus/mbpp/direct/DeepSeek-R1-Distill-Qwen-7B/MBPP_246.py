def babylonian_squareroot(n):
    """Compute the square root of n using the Babylonian method."""
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    guess = n / 2.0
    epsilon = 1e-15
    while True:
        next_guess = (guess + n / guess) / 2.0
        if abs(next_guess - guess) < epsilon:
            return next_guess
        guess = next_guess