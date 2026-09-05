import math
from typing import List


def get_gcd(numbers: List[int]) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of all integers in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The greatest common divisor of all elements in the list.

    Raises:
        ValueError: If the input list is empty or contains non-integer types.
        TypeError: If the input is not a list.
    """
    # Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list of integers, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list
    if len(numbers) == 0:
        raise ValueError("The input list must contain at least one integer.")

    # Validate that all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise ValueError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # The GCD of a single number is the absolute value of that number
    # (By convention, GCD is non-negative)
    if len(numbers) == 1:
        return abs(numbers[0])

    def compute_two_way_gcd(a: int, b: int) -> int:
        """
        Helper function to calculate GCD of two numbers using the Euclidean Algorithm.
        """
        # Work with absolute values as GCD is traditionally non-negative
        num1 = abs(a)
        num2 = abs(b)

        while num2 != 0:
            remainder = num1 % num2
            num1 = num2
            num2 = remainder
        return num1

    # Start with the absolute value of the first element
    # We use absolute values because GCD(x, y) == GCD(|x|, |y|)
    current_gcd = abs(numbers[0])

    # Iterate through the rest of the list
    # GCD(a, b, c) is equivalent to GCD(GCD(a, b), c)
    for i in range(1, len(numbers)):
        next_value = numbers[i]

        # Update current_gcd by finding the GCD of the previous 
        # result and the current element
        current_gcd = compute_two_way_gcd(current_gcd, next_value)

        # Optimization: If the GCD reaches 1, it will stay 1 
        # (unless the remaining numbers are 0, but GCD(1,0)=1)
        if current_gcd == 1:
            return 1

    return current_gcd


if __name__ == "__main__":
    # Verification of requirements
    assert get_gcd([2, 4, 6, 8, 16]) == 2
    assert get_gcd([1, 2, 3]) == 1
    assert get_gcd([2, 4, 6, 8]) == 2