def tn_ap(first_term: int, common_difference: int, term_index: int) -> int:
    """
    Calculates the n-th term of an arithmetic progression.

    Formula: a_n = a_1 + (n - 1) * d
    Where:
        a_n  = n-th term
        a_1  = first term
        d    = common difference
        n    = term index (must be a positive integer)

    Args:
        first_term (int): The first term of the sequence.
        common_difference (int): The constant added to the previous term.
        term_index (int): The position of the term to find (1-based).

    Returns:
        int: The calculated n-th term.

    Raises:
        ValueError: If term_index is less than or equal to zero.
    """

    # Validate that term_index is strictly positive
    if term_index <= 0:
        raise ValueError(
            f"The term index must be a positive integer, but received: {term_index}"
        )

    # Initialize variables with explicit names for clarity
    a_1 = first_term
    d = common_difference
    n = term_index

    # Calculate the number of intervals between the first term and the n-th term
    # This corresponds to (n - 1) in the standard formula
    number_of_intervals = n - 1

    # Calculate the total added value from the common difference
    total_difference_contribution = number_of_intervals * d

    # Calculate the final term by adding the initial term and the difference contribution
    n_th_term = a_1 + total_difference_contribution

    return n_th_term