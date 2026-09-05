def Check_Solution(a: float, b: float, c: float) -> str:
    """
    Determines whether one root of the quadratic equation ax^2 + bx + c = 0
    is exactly twice the other root.

    The function returns:
      - "Yes"  if one root is twice the other (and the equation is valid and has roots).
      - "No"   otherwise (invalid equation, no real roots, or roots do not satisfy condition).

    Mathematical derivation:
      Let the roots be r and 2r.
      By Vieta's formulas:
        r + 2r = -b/a  =>  3r = -b/a  =>  r = -b/(3a)
        r * 2r = c/a   =>  2r^2 = c/a

      Substitute r:
        2 * (-b/(3a))^2 = c/a
        2 * (b^2 / (9a^2)) = c/a
        (2 * b^2) / (9 * a^2) = c / a

      Multiply both sides by 9 * a^2:
        2 * b^2 = 9 * a * c

      Therefore, the condition is: 2 * b^2 == 9 * a * c

    Edge cases handled:
      - a == 0: Not a quadratic equation (linear or constant), so return "No".
      - Division by zero scenarios are avoided by using the derived integer-like condition.
      - Floating point precision issues: We use a small tolerance for float comparison if needed,
        but the problem examples suggest exact arithmetic expectations. However, since inputs are floats,
        we will use a tolerance to account for floating point inaccuracies while still being strict.
      - All-equal roots, negative numbers, zero values: Handled by the algebraic condition which is robust.

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant term
    :return: "Yes" if condition holds, "No" otherwise
    """

    # Step 1: Validate that 'a' is not zero.
    # If a is zero, it is not a quadratic equation.
    if a == 0.0:
        return "No"

    # Step 2: Validate that 'b' and 'c' are finite numbers (handle NaN/Inf if necessary).
    # While the problem doesn't explicitly specify non-numbers, defensive coding requires checking finiteness.
    import math

    if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(c)):
        return "No"

    # Step 3: Calculate the left-hand side (LHS) of the derived condition: 2 * b^2
    lhs = 2.0 * (b * b)

    # Step 4: Calculate the right-hand side (RHS) of the derived condition: 9 * a * c
    rhs = 9.0 * a * c

    # Step 5: Compare LHS and RHS.
    # We use a small epsilon tolerance to handle floating-point precision errors.
    # The tolerance is relative to the magnitude of the values to be robust.
    epsilon = 1e-9
    tolerance = max(abs(lhs), abs(rhs)) * epsilon

    # Check if the absolute difference is within the tolerance.
    if abs(lhs - rhs) <= tolerance:
        return "Yes"
    else:
        return "No"