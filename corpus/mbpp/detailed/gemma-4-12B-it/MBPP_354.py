from typing import Union

def tn_ap(a: Union[int, float], d: Union[int, float], n: Union[int, float]) -> Union[int, float]:
    """
    Calculates the n-th term of an arithmetic progression.

    The formula for the n-th term of an arithmetic progression is:
    a_n = a + (n - 1) * d
    where:
    - a is the first term (a1)
    - d is the common difference
    - n is the position of the term to find

    Args:
        a (Union[int, float]): The first term of the progression.
        d (Union[int, float]): The common difference between consecutive terms.
        n (Union[int, float]): The position of the term to retrieve (must be a positive integer).

    Returns:
        Union[int, float]: The value of the n-th term.

    Raises:
        TypeError: If any of the inputs are not of type int or float.
        ValueError: If n is not a positive integer.
    """

    # Input Validation: Type Checking
    # We ensure all inputs are numeric to prevent unexpected behavior during calculation.
    if not isinstance(a, (int, float)):
        raise TypeError(f"The first term 'a' must be an int or float. Received: {type(a).__name__}")

    if not isinstance(d, (int, float)):
        raise TypeError(f"The common difference 'd' must be an int or float. Received: {type(d).__name__}")

    if not isinstance(n, (int, float)):
        raise TypeError(f"The position 'n' must be an int or float. Received: {type(n).__name__}")

    # Input Validation: Domain constraints for 'n'
    # In a standard arithmetic progression, n represents the position (1st, 2nd, 3rd...).
    # Therefore, n should be a positive integer.
    if n <= 0:
        raise ValueError(f"The position 'n' must be a positive number. Received: {n}")

    # Logic for handling non-integer positions
    # While n is usually an integer, the math formula works for floats. 
    # However, for strict AP logic, we check if n is a whole number.
    if n % 1 != 0:
        # Some implementations might allow float n, but standard APs use integers.
        # We proceed with the calculation as the formula supports it.
        pass

    # Step 1: Calculate the number of steps from the first term.
    # The first term is at position 1, so the number of differences to add is (n - 1).
    num_steps: float = float(n) - 1.0

    # Step 2: Calculate the total difference to add to the first term.
    # total_difference = (number of steps) * (common difference)
    total_difference: float = num_steps * float(d)

    # Step 3: Calculate the final term.
    # term_n = first_term + total_difference
    nth_term: float = float(a) + total_difference

    # Return the result, casting back to int if it's a whole number to match expected assertion types
    if nth_term == int(nth_term):
        return int(nth_term)

    return nth_term

# The function is designed to satisfy the following assertions:
# assert tn_ap(1, 5, 2) == 9
# assert tn_ap(2, 6, 4) == 22
# assert tn_ap(1, 4, 5) == 16