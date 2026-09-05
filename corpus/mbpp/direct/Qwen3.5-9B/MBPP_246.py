def babylonian_squareroot(n, tolerance=1e-10, max_iterations=1000):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0:
        return 0.0

    guess = n / 2.0
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + n / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

    return guess