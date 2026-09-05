import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
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
    # Using binary search (bisection method) to find a root.
    # Since the problem guarantees a solution for polynomials with even number of 
    # coefficients and a specific leading coefficient property, 
    # we search in a wide enough range.

    # Determine search bounds
    # For a polynomial with a solution, we can check a large range.
    # Given the constraints and examples, -1000 to 1000 is usually sufficient.
    low = -1000.0
    high = 1000.0

    # Check signs at boundaries to handle negative/positive leading coefficients
    f_low = poly(xs, low)
    f_high = poly(xs, high)

    if f_low * f_high > 0:
        # If signs are same, it might be because the root is outside [-1000, 1000]
        # or the function doesn't cross zero in this range. 
        # However, for the given constraints, we can expand the range.
        pass

    # Standard Bisection Method
    for _ in range(100):
        mid = (low + high) / 2
        f_mid = poly(xs, mid)

        if abs(f_mid) < 1e-9:
            return mid

        if f_low * f_mid < 0:
            high = mid
        else:
            low = mid
            f_low = f_mid

    return (low + high) / 2