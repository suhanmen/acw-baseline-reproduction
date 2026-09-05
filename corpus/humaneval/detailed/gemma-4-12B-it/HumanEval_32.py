import math
from typing import List


def poly(xs: List[float], x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    total_sum = 0.0
    for i, coeff in enumerate(xs):
        total_sum += coeff * math.pow(x, i)
    return total_sum


def find_zero(xs: List[float]) -> float:
    """
    xs are coefficients of a polynomial.
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
    # Input Validation: Check if the list is empty
    if not xs:
        raise ValueError("The input list of coefficients cannot be empty.")

    # Input Validation: Check if the number of coefficients is even
    # The problem statement specifies that find_zero only takes lists with even numbers of coefficients.
    if len(xs) % 2 != 0:
        raise ValueError("The input list must have an even number of coefficients.")

    # Check if all coefficients are zero (degenerate case)
    is_all_zero = True
    for coeff in xs:
        if coeff != 0:
            is_all_zero = False
            break

    if is_all_zero:
        # If all coefficients are 0, any x is a root. By convention, return 0.0.
        return 0.0

    # Numerical Method: Bisection Method
    # We need to find a range [a, b] where the polynomial changes sign.
    # Since the problem guarantees a solution exists, we look for a bracket.

    # Define bounds for search.
    # Cauchy's bound for roots: |x| <= 1 + max(|a_n|, ..., |a_1|) / |a_n|
    # However, to keep it simple and robust for the provided examples, 
    # we can start with a reasonably large range and expand if needed.

    low = -1000.0
    high = 1000.0

    # Step 1: Find a bounding interval where poly(low) and poly(high) have opposite signs.
    # If not found, expand the bounds.
    found_bracket = False
    initial_bounds = [low, high]

    while not found_bracket and abs(low) < 1e9:
        val_low = poly(xs, low)
        val_high = poly(xs, high)

        if val_low * val_high <= 0:
            found_bracket = True
        else:
            # Expand the search range exponentially
            low *= 2
            high *= 2
            if low < 0:
                low -= abs(low) # ensure it stays negative
            else:
                low = -abs(low)
            # high remains positive or grows

    # If we can't find a bracket in the standard expansion, 
    # it's a very extreme case, but the problem guarantees a solution.
    if not found_bracket:
        # Fallback to a very wide range if expansion logic is tricky
        low = -1e6
        high = 1e6

    # Step 2: Perform Bisection Method
    # Tolerance for the zero finding
    tolerance = 1e-9
    max_iterations = 100

    current_low = low
    current_high = high

    for _ in range(max_iterations):
        mid = (current_low + current_high) / 2.0
        val_mid = poly(xs, mid)

        # Check if the midpoint is close enough to zero
        if abs(val_mid) < 1e-12 or (current_high - current_low) / 2.0 < tolerance:
            return mid

        # Determine which side to keep
        val_low = poly(xs, current_low)

        if (val_low > 0 and val_mid < 0) or (val_low < 0 and val_mid > 0):
            current_high = mid
        else:
            current_low = mid

    return (current_low + current_high) / 2.0