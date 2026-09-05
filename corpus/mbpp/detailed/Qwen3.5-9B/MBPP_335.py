def _validate_inputs(first_term, last_term, number_of_terms):
    """
    Validates the inputs for the arithmetic progression sum calculation.

    Args:
        first_term (int): The first term of the arithmetic progression.
        last_term (int): The last term of the arithmetic progression.
        number_of_terms (int): The number of terms in the progression.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If number_of_terms is non-positive.
    """
    # Check for correct types
    if not isinstance(first_term, int):
        raise TypeError(f"Expected first_term to be an integer, got {type(first_term).__name__}")
    if not isinstance(last_term, int):
        raise TypeError(f"Expected last_term to be an integer, got {type(last_term).__name__}")
    if not isinstance(number_of_terms, int):
        raise TypeError(f"Expected number_of_terms to be an integer, got {type(number_of_terms).__name__}")

    # Check for valid count
    if number_of_terms <= 0:
        raise ValueError(f"Expected number_of_terms to be a positive integer, got {number_of_terms}")


def _calculate_arithmetic_sum(first_term, last_term, number_of_terms):
    """
    Calculates the sum of an arithmetic progression using the standard formula.

    The formula for the sum S of an arithmetic progression is:
    S = (n / 2) * (a + l)
    where:
    n = number of terms
    a = first term
    l = last term

    Args:
        first_term (int): The first term of the progression.
        last_term (int): The last term of the progression.
        number_of_terms (int): The number of terms in the progression.

    Returns:
        int: The calculated sum of the progression.
    """
    # Apply the arithmetic series sum formula: S = n * (a + l) / 2
    sum_numerator = number_of_terms * (first_term + last_term)
    total_sum = sum_numerator // 2

    return total_sum


def ap_sum(first_term, last_term, number_of_terms):
    """
    Calculates the sum of an arithmetic progression given the first term,
    the last term, and the number of terms.

    The function assumes the progression is well-defined by these three parameters.
    It does not verify if the terms actually form a consistent arithmetic sequence
    (e.g., it does not check if the common difference derived from consecutive terms
    is constant), as the problem statement implies a direct calculation based on
    the provided bounds and count. However, it strictly validates the inputs.

    Args:
        first_term (int): The first term of the arithmetic progression.
        last_term (int): The last term of the arithmetic progression.
        number_of_terms (int): The number of terms in the progression.

    Returns:
        int: The sum of the arithmetic progression.

    Examples:
        >>> ap_sum(1, 5, 2)
        25
        >>> ap_sum(2, 6, 4)
        72
        >>> ap_sum(1, 4, 5)
        34
    """
    # Step 1: Validate all input arguments to ensure they are integers and logically sound.
    _validate_inputs(first_term, last_term, number_of_terms)

    # Step 2: Calculate the sum using the arithmetic series formula.
    # Formula: Sum = n * (first + last) / 2
    result = _calculate_arithmetic_sum(first_term, last_term, number_of_terms)

    return result