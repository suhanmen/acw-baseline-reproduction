from typing import List

def ap_sum(first_term: int, last_term: int, common_difference: int) -> int:
    """
    Calculates the sum of an arithmetic progression.

    The formula for the sum of an arithmetic progression is:
    S = (n / 2) * (a + l)
    where:
    - n is the number of terms
    - a is the first term
    - l is the last term

    Args:
        first_term (int): The starting value of the sequence.
        last_term (int): The ending value of the sequence.
        common_difference (int): The difference between consecutive terms.

    Returns:
        int: The sum of the arithmetic progression.

    Raises:
        ValueError: If inputs are logically inconsistent or result in an 
                    impossible sequence (e.g., zero difference with different terms).
    """

    # Validate inputs for basic types (though type hints are present)
    if not isinstance(first_term, int) or \
       not isinstance(last_term, int) or \
       not isinstance(common_difference, int):
        raise ValueError("All inputs (first_term, last_term, common_difference) must be integers.")

    # Case 1: The first term and last term are the same.
    # This is a sequence of 1 term (or infinite terms of same value if diff is 0).
    # Standard AP interpretation: if first == last, the sum is just the value.
    if first_term == last_term:
        # Special case: if difference is non-zero, this only happens if n=1.
        # If difference is zero, it's technically an infinite sequence, 
        # but for calculation we assume the range is closed.
        return first_term

    # Case 2: Common difference is zero.
    # If common difference is zero but terms are different, it's an impossible sequence.
    if common_difference == 0:
        raise ValueError("Common difference cannot be zero if first_term and last_term are different.")

    # Calculate the number of terms (n).
    # The formula for the n-th term is: l = a + (n - 1) * d
    # Rearranging for n: n = ((l - a) / d) + 1

    total_difference = last_term - first_term

    # Check if the last_term is actually reachable from first_term with the given difference.
    # The total difference must be perfectly divisible by the common difference.
    if total_difference % common_difference != 0:
        raise ValueError(
            f"The last_term {last_term} is not reachable from first_term {first_term} "
            f"with a common_difference of {common_difference}."
        )

    # Calculate n
    # Using integer division because we've verified divisibility above.
    num_terms = (total_difference // common_difference) + 1

    # The number of terms must be positive.
    # This handles cases where the direction of the sequence is inconsistent
    # (e.g., first_term < last_term but common_difference is negative).
    if num_terms <= 0:
        raise ValueError(
            f"Sequence is impossible: first_term {first_term}, "
            f"last_term {last_term}, and difference {common_difference} "
            f"result in a non-positive number of terms."
        )

    # Calculate the sum using the formula: S = (n * (a + l)) / 2
    # We use integer division at the end because the sum of an AP 
    # of integers is always an integer.
    sum_of_terms = num_terms * (first_term + last_term)
    total_sum = sum_of_terms // 2

    return total_sum