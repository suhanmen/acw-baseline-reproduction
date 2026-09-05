from typing import Union

def tetrahedral_number(n: Union[int, float]) -> float:
    """
    Calculates the nth tetrahedral number.

    The tetrahedral number is a figurate number that represents a pyramid 
    with a triangular base. The nth tetrahedral number is the sum of the 
    first n triangular numbers.

    Formula: T_n = (n * (n + 1) * (n + 2)) / 6

    Args:
        n (Union[int, float]): The position in the sequence (must be a non-negative integer).

    Returns:
        float: The nth tetrahedral number.

    Raises:
        ValueError: If n is negative or not a whole number.
        TypeError: If n is not an integer or a float.
    """
    # 1. Validate input type
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input 'n' must be a number, received {type(n).__name__}")

    # 2. Validate that the input is a mathematical integer (e.g., 5.0 is okay, 5.5 is not)
    if not float(n).is_integer():
        raise ValueError(f"Input 'n' must be a whole number, received {n}")

    # 3. Convert to integer for consistent calculation
    n_int = int(n)

    # 4. Handle boundary cases for negative values
    if n_int < 0:
        raise ValueError(f"Input 'n' must be non-negative, received {n_int}")

    # 5. Handle the edge case of 0
    # The 0th tetrahedral number is 0.
    if n_int == 0:
        return 0.0

    # 6. Handle the edge case of 1
    # The 1st tetrahedral number is 1.
    if n_int == 1:
        return 1.0

    # 7. Calculate the tetrahedral number using the formula:
    # T_n = (n * (n + 1) * (n + 2)) / 6
    # We use explicit steps to ensure clarity and avoid precision issues with large numbers.

    term_one = n_int
    term_two = n_int + 1
    term_three = n_int + 2

    # Calculate the product of the three consecutive integers
    product = term_one * term_two * term_three

    # The result is the product divided by 6
    result = float(product) / 6.0

    return result

# The following assertions verify the requirements:
if __name__ == "__main__":
    assert tetrahedral_number(5) == 35.0
    assert tetrahedral_number(6) == 56.0
    assert tetrahedral_number(7) == 84.0