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

    # Step 1: Validate input list is not empty
    if not xs:
        raise ValueError("Input list of coefficients cannot be empty.")

    # Step 2: Validate input list has at least one element (redundant check but explicit)
    if len(xs) < 1:
        raise ValueError("Input list must contain at least one coefficient.")

    # Step 3: Check if the number of coefficients is even, as guaranteed by problem constraints
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")

    # Step 4: Find the largest absolute value among coefficients to establish bounds if needed
    # Although the problem guarantees a solution, we check for trivial cases where all are zero.
    max_abs_coeff = 0.0
    for coeff in xs:
        if abs(coeff) > max_abs_coeff:
            max_abs_coeff = abs(coeff)

    # Step 5: Handle the degenerate case where all coefficients are zero
    # In this case, any x is technically a root, but we return 0 as a canonical solution.
    if max_abs_coeff == 0.0:
        return 0.0

    # Step 6: Define helper function to evaluate the polynomial
    def evaluate_polynomial(coefficients: list, value_x: float) -> float:
        result = 0.0
        power_of_x = 1.0
        for coeff in coefficients:
            result += coeff * power_of_x
            power_of_x *= value_x
        return result

    # Step 7: Implement bisection method to find the root
    # Since the problem guarantees a solution for even degree polynomials with given constraints,
    # we can search within a bounded interval. A safe initial interval is often [-2*max_coeff, 2*max_coeff]
    # or derived from coefficient magnitudes. However, a robust approach for guaranteed roots in such problems
    # often utilizes the property that roots lie within a specific range relative to coefficients.
    # For safety, let's expand our search range dynamically until we find signs at both ends.

    lower_bound = -10000.0
    upper_bound = 10000.0
    threshold = 1e-6  # Tolerance for determining sign change

    # Ensure the polynomial evaluates to different signs at the boundaries of our search space
    # If not, expand the search space.
    try:
        y_lower = evaluate_polynomial(xs, lower_bound)
        y_upper = evaluate_polynomial(xs, upper_bound)
    except OverflowError:
        raise ValueError("Coefficients or evaluation range caused numerical overflow.")

    # Step 8: Expand bounds until a sign change is detected or maximum reasonable expansion is reached
    # The problem statement implies a root exists, so we assume a large enough bound will capture the sign change.
    # We'll cap the expansion to prevent infinite loops in pathological floating point cases,
    # though mathematically a root is guaranteed.
    expansion_factor = 2.0
    max_expansions = 100

    for _ in range(max_expansions):
        # Recalculate values at new bounds
        # Using the expanded bounds directly
        current_lower = lower_bound
        current_upper = upper_bound

        # Evaluate at current bounds
        val_lower = evaluate_polynomial(xs, current_lower)
        val_upper = evaluate_polynomial(xs, current_upper)

        # Check for sign change
        # We treat very small values close to zero as having the same sign as the larger magnitude value
        # to avoid false positives due to noise, but here we look for strict sign difference for robustness.
        # If one value is positive and the other negative, a root exists between them.

        if (val_lower > 0 and val_upper < 0) or (val_lower < 0 and val_upper > 0):
            # Sign change detected, proceed to bisection
            break

        # If no sign change, expand the range
        lower_bound = current_lower * expansion_factor
        upper_bound = current_upper * expansion_factor

        # Safety break if expansion becomes excessively large without sign change (shouldn't happen per problem spec)
        if abs(lower_bound) > 1e20 or abs(upper_bound) > 1e20:
            # Fallback: if we still can't find signs, assume root is at 0 or try to find min/max
            # But per problem guarantee, this branch is theoretically unreachable for valid inputs.
            # We return 0 as a last resort fallback.
            return 0.0

    # Step 9: Perform Bisection Method to find the root within [lower_bound, upper_bound]
    # Initialize mid point
    min_val = lower_bound
    max_val = upper_bound

    # Loop until the interval is sufficiently small
    iterations = 0
    max_iterations = 1000
    tolerance = 1e-7

    while (max_val - min_val) / 2.0 > tolerance and iterations < max_iterations:
        iterations += 1
        mid = (min_val + max_val) / 2.0

        f_mid = evaluate_polynomial(xs, mid)

        # If f(mid) is close enough to zero, we can stop
        if abs(f_mid) < threshold:
            return mid

        # Evaluate at the current endpoints to ensure logic holds during narrowing
        f_min = evaluate_polynomial(xs, min_val)
        f_max = evaluate_polynomial(xs, max_val)

        # Determine which half contains the root
        # If f(mid) and f(min_val) have opposite signs, root is in [min_val, mid]
        if (f_min * f_mid) < 0:
            max_val = mid
        else:
            # Otherwise, root is in [mid, max_val]
            # This assumes f(mid) and f(max_val) have opposite signs, which is guaranteed by the loop setup
            min_val = mid

    # Step 10: Return the final approximation
    return (min_val + max_val) / 2.0