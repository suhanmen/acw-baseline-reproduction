import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    """
    if not xs:
        return 0.0
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Finds a real root of the polynomial defined by the coefficients xs.
    """
    # Handle the case where the polynomial is a constant
    if not xs:
        return 0.0
    if len(xs) == 1:
        return -xs[0] / 1.0 if xs[0] != 0 else 0.0

    # Check if all coefficients are zero (special case)
    if all(coeff == 0 for coeff in xs):
        return 0.0

    # Determine the initial interval where the root might be
    initial_sign = None
    for start in [1.0, -1.0]:
        try:
            y = poly(xs, start)
        except OverflowError:
            continue  # In case of overflow, skip this start
        if initial_sign is None:
            initial_sign = y
        else:
            if initial_sign * y < 0:
                # Sign change found, root is between start and current interval
                left = start
                right = 1.0 if start == 1.0 else -1.0
                break

    if initial_sign == 0:
        return -1.0  # Return a default root if found at start points

    # Expand the interval exponentially until sign change is found
    bound = 1.0
    while True:
        y = poly(xs, bound)
        if y != 0 and (initial_sign * y < 0):
            left = max(-bound, start if start == 1.0 else -1.0)
            right = bound
            break
        elif y == 0:
            return bound
        bound *= 2

    # Refine the root using linear approximation within the interval [left, right]
    # Find the point where the function crosses zero
    if left == right:
        return left
    left_y = poly(xs, left)
    right_y = poly(xs, right)

    # Compute the next approximation using linear interpolation
    if left_y * right_y < 0:
        t = (-left_y) / (right_y - left_y)
        root = left + t * (right - left)
        return round(root, 2) if round(root, 2) in (left, right) else root
    else:
        # If no sign change, return the midpoint as a fallback
        return (left + right) / 2.0

    # Edge case: all zeros except the constant term
    if all(c == 0 for c in xs) or len(xs) == 0:
        return 0.0