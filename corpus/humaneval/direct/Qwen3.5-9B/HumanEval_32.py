import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    low = float('-inf')
    high = float('inf')

    # Find a bracket [low, high] such that poly(low) and poly(high) have opposite signs
    if poly(xs, 0) == 0:
        return 0.0

    if poly(xs, 1) * poly(xs, -1) < 0:
        low, high = -1, 1
    else:
        # Expand the interval until a sign change is found
        step = 1
        while poly(xs, step) * poly(xs, -step) >= 0:
            step *= 2
            low = -step
            high = step

    # Bisection method to find the root
    for _ in range(100):  # Sufficient iterations for high precision
        mid = (low + high) / 2
        if poly(xs, mid) == 0:
            return mid
        if poly(xs, low) * poly(xs, mid) < 0:
            high = mid
        else:
            low = mid

    return (low + high) / 2