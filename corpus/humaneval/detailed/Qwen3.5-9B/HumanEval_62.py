from typing import List, Union

Number = Union[int, float]

def _validate_polynomial_coefficients(xs: List) -> None:
    """
    Validates that the input list represents valid polynomial coefficients.

    Rules:
    - Must be a list.
    - Must not be None.
    - Must not contain non-numeric values (only int or float allowed).
    - Does not strictly enforce non-zero length or specific ordering here,
      as those are handled in the derivative logic or result naturally.

    Raises:
        TypeError: If the input is not a list or contains invalid types.
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(xs, list):
        raise TypeError(f"Input must be a list, got {type(xs).__name__} instead.")

    if len(xs) == 0:
        raise ValueError("Input list cannot be empty; a polynomial must have at least one coefficient.")

    for i, coeff in enumerate(xs):
        if not isinstance(coeff, (int, float)) or isinstance(coeff, bool):
            raise TypeError(
                f"Coefficient at index {i} is of invalid type {type(coeff).__name__}. "
                f"Only integers and floats are allowed."
            )

def _compute_derivative_coefficients(xs: List[Number]) -> List[Number]:
    """
    Computes the coefficients of the derivative of the polynomial.

    Logic:
    - The derivative of a term a_n * x^n is n * a_n * x^(n-1).
    - The constant term (n=0) becomes 0 and is removed from the result.
    - We iterate through the input list starting from index 1.

    Args:
        xs: List of coefficients [a0, a1, a2, ...]

    Returns:
        List of coefficients for the derivative polynomial.
    """
    n_terms = len(xs)

    # A constant polynomial (only one term) has a derivative of 0.
    # We represent 0 as an empty list to be consistent with the pattern
    # where we strip the constant term. Alternatively, we could return [0].
    # Looking at the problem examples: [3,1,2,4,5] -> [1, 4, 12, 20].
    # [1, 2, 3] (1 + 2x + 3x^2) -> 2 + 6x -> [2, 6].
    # If input is [5] (5), derivative is 0.
    # Convention in such problems often returns [] for 0 polynomial 
    # or [0]. Given the stripping of the constant term in the examples,
    # returning [] for a constant input is the logical extension.

    if n_terms <= 1:
        return []

    derivative_coeffs: List[Number] = []

    for i in range(1, n_terms):
        # The power of x for the current term xs[i] is 'i'.
        current_power = i

        # The original coefficient is xs[i].
        original_coefficient = xs[i]

        # Apply power rule: d/dx (a * x^n) = n * a * x^(n-1)
        new_coefficient = current_power * original_coefficient

        derivative_coeffs.append(new_coefficient)

    return derivative_coeffs

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Step 1: Validate the input strictly before processing.
    _validate_polynomial_coefficients(xs)

    # Step 2: Compute the new coefficients based on the power rule.
    result = _compute_derivative_coefficients(xs)

    # Step 3: Return the computed list.
    return result