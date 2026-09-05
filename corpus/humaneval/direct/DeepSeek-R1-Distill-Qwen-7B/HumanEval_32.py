import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds an x such that poly(x) = 0.
    """
    # The degree of the polynomial is len(xs) - 1, which is even.
    # The leading coefficient determines the behavior at infinity.
    # We search between 0 and a sufficiently large number, say 1e6, to find a sign change.
    # Once a sign change is found, apply the bisection method to find the root.
    # The function ensures an even number of coefficients and that the largest coefficient is non-zero.
    # Hence, by the Intermediate Value Theorem, a root exists.

    # First, find an interval where the function changes sign.
    a = 0.0
    b = 1.0
    # Ensure that f(b) and f(a) have opposite signs.
    # Since the polynomial must cross zero, this interval will contain at least one root.
    fa = poly(xs, a)
    fb = poly(xs, b)
    if not (fa * fb < 0):
        # If no sign change in initial interval, expand the interval.
        b = 2.0
        while fa * fb >= 0:
            b *= 2.0
            fb = poly(xs, b)
            if fb == 0:
                return round(b, 2)  # Exact root found at b
            # Prevent infinite loop in case of no sign change (though problem statement ensures one)
            if b > 1e6:
                break
    # Now perform bisection between a and b
    epsilon = 1e-6  # Desired precision
    for _ in range(100):  # Maximum 100 iterations for precision
        c = (a + b) / 2
        fc = poly(xs, c)
        if fc == 0 or (b - a) / 2 < epsilon:
            return round(c, 2)
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    # Return rounded result
    return round(c, 2)