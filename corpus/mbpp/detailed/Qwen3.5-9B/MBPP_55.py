def _validate_positive_integer(value: int, name: str) -> None:
    """
    Validate that a given value is a positive integer.

    If the value is not a positive integer, raises a ValueError with a descriptive message.

    Args:
        value: The value to check.
        name: The name of the parameter for the error message.

    Raises:
        ValueError: If the value is not a positive integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"The {name} must be an integer. Got {type(value).__name__}.")
    if value <= 0:
        raise ValueError(f"The {name} must be a positive integer (> 0). Got {value}.")


def _validate_number(value, name: str) -> None:
    """
    Validate that a given value is a real number.

    If the value is not a number (int or float), raises a TypeError.

    Args:
        value: The value to check.
        name: The name of the parameter for the error message.

    Raises:
        TypeError: If the value is not a number.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"The {name} must be a number (int or float). Got {type(value).__name__}.")
    if isinstance(value, float) and (not value.isfinite()):
        raise ValueError(f"The {name} must be a finite number. Got {value}.")


def _validate_non_zero_denominator(base: float) -> None:
    """
    Validate that the base of the geometric series is non-zero.

    A geometric series with a zero base is degenerate (all terms are zero) and 
    typically not useful for finding the n-th term in a standard context. 
    Furthermore, if the first term was derived from a division by zero, it implies an issue.
    However, strictly speaking, 0, 0, 0... is a geometric series. 
    But usually, the 'base' (common ratio) cannot be 0 if we are talking about a standard progression 
    starting with a non-zero term, or if the term index is large.
    Let's enforce base != 0 to avoid ambiguity and division by zero in potential extensions,
    though for simple a_n = a_1 * r^(n-1), r=0 works mathematically (result 0 for n>1).
    Given the assertions use positive integers, we will enforce base != 0 for robustness.

    Args:
        base: The common ratio (base).

    Raises:
        ValueError: If the base is zero.
    """
    if base == 0:
        raise ValueError("The common ratio (base) of the geometric series cannot be zero.")


def calculate_nth_term(term_index: int, first_term: float, common_ratio: float) -> float:
    """
    Calculate the n-th term of a geometric series.

    Formula: a_n = a_1 * r^(n-1)

    Args:
        term_index (int): The position of the term to find (1-based index).
        first_term (float): The first term of the series (a_1).
        common_ratio (float): The common ratio of the series (r).

    Returns:
        float: The value of the n-th term.

    Raises:
        ValueError: If inputs are invalid (see _validate functions).
        TypeError: If inputs are of wrong types.
    """

    # Step 1: Validate term_index
    # Must be a positive integer (1, 2, 3, ...)
    _validate_positive_integer(term_index, "term_index")

    # Step 2: Validate first_term
    # Can be any number, but cannot be NaN or Inf for meaningful calculation
    _validate_number(first_term, "first_term")

    # Step 3: Validate common_ratio
    # Cannot be zero (as per requirement for standard geometric series properties in this context)
    _validate_non_zero_denominator(common_ratio)

    # Step 4: Compute the exponent (n - 1)
    exponent = term_index - 1

    # Step 5: Calculate r raised to the power of (n - 1)
    ratio_powered = common_ratio ** exponent

    # Step 6: Calculate the final term
    result = first_term * ratio_powered

    return result


def tn_gp(n: int, a1: float, r: float) -> float:
    """
    Wrapper function to find the n-th term of a geometric series with explicit documentation.
    Matches the signature requirement: tn_gp(term_index, first_term, common_ratio).

    Args:
        n: The term number to retrieve (must be >= 1).
        a1: The first term of the series.
        r: The common ratio of the series.

    Returns:
        The value of the n-th term.
    """
    return calculate_nth_term(n, a1, r)