from typing import List


def is_even_digit(number: int) -> bool:
    """
    Checks if a number consists only of even digits.
    The problem asks for "even digits" between a and b.
    Based on the examples:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(10, 14) => []

    This implies that the numbers themselves must be single-digit even 
    integers. However, a strict reading of "even digits between a and b" 
    could mean numbers where all digits are even, or just single-digit 
    even numbers. 

    Given the example 10-14 returns [], it confirms that multi-digit 
    numbers are excluded, or specifically, numbers that are not single 
    digits are not considered valid even digits in this context.
    """
    # Check if the number is a single digit
    is_single_digit = 0 <= number <= 9

    # Check if it is even
    is_even = number % 2 == 0

    return is_single_digit and is_even


def validate_inputs(a: int, b: int) -> None:
    """
    Validates that the inputs are integers and non-negative.
    Raises ValueError if inputs are invalid.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    if a < 0 or b < 0:
        raise ValueError("Both inputs must be positive integers (or zero).")


def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # 1. Validate inputs
    validate_inputs(a, b)

    # 2. Determine the range boundaries
    # The problem implies a range [min(a, b), max(a, b)] inclusive.
    lower_bound = min(a, b)
    upper_bound = max(a, b)

    # 3. Initialize the container for results
    even_digits_list = []

    # 4. Iterate through the range
    # We check every integer from lower_bound to upper_bound.
    for current_number in range(lower_bound, upper_bound + 1):
        # Check if the number qualifies as an even digit.
        # Based on the provided examples:
        # - 2, 4, 6, 8 are included.
        # - 10, 12, 14 are excluded (even though they are even).
        # This confirms we are looking for single-digit even numbers.

        is_valid_even_digit = is_even_digit(current_number)

        if is_valid_even_digit:
            even_digits_list.append(current_number)

    # 5. Ensure the list is in ascending order
    # Since we iterated from lower_bound to upper_bound, it's already sorted,
    # but we can explicitly sort to guarantee the requirement.
    even_digits_list.sort()

    return even_digits_list