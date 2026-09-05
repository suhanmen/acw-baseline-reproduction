from typing import List, Union


def derivative(xs: list) -> List[Union[int, float]]:
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Validate input type
    if not isinstance(xs, list):
        raise TypeError("Input must be a list of numerical coefficients.")

    # Handle edge case: Empty list
    # The derivative of a zero-degree null polynomial is typically 0 or an empty representation.
    # Based on the pattern of the examples, an empty or constant list returns an empty list.
    if len(xs) == 0:
        return []

    # Handle edge case: Single element (constant term)
    # The derivative of a constant C is 0.
    # Following the logic of the problem, if the result is a constant 0, 
    # and we represent the polynomial as [a0, a1, ...], 
    # then derivative of [C] is [0] or []. 
    # Looking at the examples: derivative([1, 2, 3]) -> [2, 6].
    # The length decreases by 1. Thus, derivative([C]) should be [].
    if len(xs) == 1:
        return []

    # Ensure all elements are numbers (int or float)
    for item in xs:
        if not isinstance(item, (int, float)):
            raise ValueError(f"All coefficients must be numeric. Found: {type(item)}")

    # The power rule for polynomials:
    # If P(x) = a0 + a1*x + a2*x^2 + a3*x^3 + ... + an*x^n
    # Then P'(x) = a1 + 2*a2*x + 3*a3*x^2 + ... + n*an*x^(n-1)

    # We ignore xs[0] because its derivative is 0.
    # The new first coefficient (constant term) is xs[1].
    # The new second coefficient (linear term) is 2 * xs[2].
    # The new i-th coefficient (index k) is (k+1) * xs[k+1].

    derivative_coeffs = []

    # We start from the second element of the original list (index 1)
    # up to the last element.
    for i in range(1, len(xs)):
        # current_coefficient represents xs[i]
        current_coefficient = xs[i]

        # The exponent of x associated with xs[i] is 'i'.
        # The derivative rule is: d/dx (a * x^i) = i * a * x^(i-1).
        power = i

        # Calculate the new coefficient for the derivative polynomial.
        # The term (xs[i] * x^i) becomes (i * xs[i] * x^(i-1)).
        # In the new list, this will be at index (i-1).
        new_val = power * current_coefficient

        derivative_coeffs.append(new_val)

    return derivative_coeffs