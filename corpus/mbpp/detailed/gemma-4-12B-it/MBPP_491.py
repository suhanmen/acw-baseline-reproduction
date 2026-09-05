from typing import Union

def sum_gp(first_term: Union[int, float], common_ratio: Union[int, float], num_terms: int) -> Union[int, float]:
    """
    Calculates the sum of a geometric progression series.

    A geometric progression is a sequence of numbers where each term after the 
    first is found by multiplying the previous one by a fixed, non-zero number 
    called the common ratio.

    The formula for the sum (S_n) is:
    S_n = a * (1 - r^n) / (1 - r)  for r != 1
    S_n = a * n                    for r == 1

    Args:
        first_term (Union[int, float]): The first term of the series (a).
        common_ratio (Union[int, float]): The ratio between consecutive terms (r).
        num_terms (int): The number of terms to sum (n).

    Returns:
        Union[int, float]: The sum of the geometric progression.

    Raises:
        ValueError: If num_terms is less than 1.
        TypeError: If inputs are not of the correct numeric types.
    """

    # --- Input Validation ---

    # Validate first_term and common_ratio are numeric
    if not isinstance(first_term, (int, float)):
        raise TypeError(f"First term must be an int or float, got {type(first_term)}")

    if not isinstance(common_ratio, (int, float)):
        raise TypeError(f"Common ratio must be an int or float, got {type(common_ratio)}")

    # Validate num_terms is an integer
    if not isinstance(num_terms, int):
        raise TypeError(f"Number of terms must be an integer, got {type(num_terms)}")

    # Validate num_terms is a positive count
    if num_terms < 0:
        raise ValueError("Number of terms cannot be negative.")

    # --- Edge Case Handling ---

    # Case 1: Zero terms results in a sum of zero
    if num_terms == 0:
        return 0

    # Case 2: First term is zero results in a sum of zero
    if first_term == 0:
        return 0

    # --- Logic Implementation ---

    # Handle the case where common_ratio is 1
    # Using the standard formula results in division by zero error
    if common_ratio == 1:
        # Sum = first_term + first_term + ... + first_term (n times)
        total_sum = first_term * num_terms
        return total_sum

    # Standard Geometric Series Formula: S_n = a * (1 - r^n) / (1 - r)
    # We break this down into steps for clarity and to avoid precision loss

    # Calculate r raised to the power of n
    ratio_to_power = common_ratio ** num_terms

    # Calculate the numerator: (1 - r^n)
    numerator = 1 - ratio_to_power

    # Calculate the denominator: (1 - r)
    denominator = 1 - common_ratio

    # Calculate the factor: (1 - r^n) / (1 - r)
    # Note: Since common_ratio != 1, denominator is guaranteed non-zero.
    multiplier = numerator / denominator

    # Calculate final sum
    total_sum = first_term * multiplier

    # If the result is mathematically an integer (e.g., 31.0), 
    # we can return it as an int if the input was integers, but 
    # for general production use, maintaining float is safer unless 
    # specifically required otherwise. Python's float/int handling 
    # will manage the transition naturally.

    return total_sum

if __name__ == "__main__":
    # The following assertions are provided by the problem statement
    assert sum_gp(1, 5, 2) == 31
    assert sum_gp(1, 5, 4) == 341
    assert sum_gp(2, 6, 3) == 728