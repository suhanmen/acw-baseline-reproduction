from typing import Any

def opposite_Signs(num1: int, num2: int) -> bool:
    """
    Determines whether two integers have opposite signs.

    A positive number and a negative number have opposite signs.
    Zero is treated as having a non-negative sign in most contexts, 
    but specifically for "opposite signs," a number is typically 
    considered opposite to another if one is strictly greater than zero 
    and the other is strictly less than zero.

    Args:
        num1 (int): The first integer to check.
        num2 (int): The second integer to check.

    Returns:
        bool: True if one number is positive and the other is negative, False otherwise.

    Raises:
        TypeError: If inputs are not integers.
    """
    # Input Validation: Ensure both inputs are integers.
    # Production-grade code should validate types to prevent unexpected behavior.
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError(f"Both arguments must be integers. Received: {type(num1)} and {type(num2)}")

    # Define helper check for strictly positive
    def is_strictly_positive(n: int) -> bool:
        return n > 0

    # Define helper check for strictly negative
    def is_strictly_negative(n: int) -> bool:
        return n < 0

    # Logic:
    # Two numbers have opposite signs if:
    # (Number 1 is positive AND Number 2 is negative) OR
    # (Number 1 is negative AND Number 2 is positive)

    num1_is_positive = is_strictly_positive(num1)
    num1_is_negative = is_strictly_negative(num1)

    num2_is_positive = is_strictly_positive(num2)
    num2_is_negative = is_strictly_negative(num2)

    # Condition 1: num1 is (+) and num2 is (-)
    case_one = num1_is_positive and num2_is_negative

    # Condition 2: num1 is (-) and num2 is (+)
    case_two = num1_is_negative and num2_is_positive

    # The result is True if either specific opposite condition is met.
    # This correctly handles:
    # - (1, -2) -> True
    # - (3, 2)  -> False (both positive)
    # - (-10, -10) -> False (both negative)
    # - (0, -1) -> False (0 is neither strictly positive nor strictly negative)
    # - (0, 1)  -> False
    # - (0, 0)  -> False

    has_opposite_signs = case_one or case_two

    return has_opposite_signs

if __name__ == "__main__":
    # Testing the requirements provided in the prompt
    assert opposite_Signs(1, -2) == True
    assert opposite_Signs(3, 2) == False
    assert opposite_Signs(-10, -10) == False