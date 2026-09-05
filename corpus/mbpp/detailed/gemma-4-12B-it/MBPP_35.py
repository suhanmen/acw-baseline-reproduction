from typing import List

def is_valid_n(n: int) -> bool:
    """
    Validates if the input n is a valid positive integer.
    The n-th rectangular number is defined for n >= 1.
    """
    if not isinstance(n, int):
        return False
    if n < 1:
        return False
    return True

def calculate_rect_num(n: int) -> int:
    """
    Calculates the n-th rectangular number.
    A rectangular number (also known as a pronic number) is a number 
    which is the product of two consecutive integers: n * (n + 1).

    Args:
        n (int): The position in the sequence (starting from 1).

    Returns:
        int: The n-th rectangular number.

    Raises:
        ValueError: If n is less than 1 or not an integer.
    """
    # Validate the input explicitly
    if not is_valid_n(n):
        raise ValueError(f"Input must be a positive integer. Received: {n}")

    # The sequence of rectangular numbers is:
    # 1st: 1 * 2 = 2
    # 2nd: 2 * 3 = 6
    # 3rd: 3 * 4 = 12
    # 4th: 4 * 5 = 20
    # 5th: 5 * 6 = 30
    # 6th: 6 * 7 = 42

    # Step 1: Identify the first factor (n)
    first_factor = n

    # Step 2: Identify the second factor (n + 1)
    second_factor = n + 1

    # Step 3: Calculate the product
    rect_num = first_factor * second_factor

    return rect_num

def find_rect_num(n: int) -> int:
    """
    Finds the n-th rectangular number.

    Example assertions:
    assert find_rect_num(4) == 20
    assert find_rect_num(5) == 30
    assert find_rect_num(6) == 42
    """
    # We delegate the core logic to the helper to maintain clean separation.
    # Any pre-processing or global logging could be done here.
    result = calculate_rect_num(n)
    return result