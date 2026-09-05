from typing import Tuple

def _is_even(digit: int) -> bool:
    """
    Helper function to determine if a single digit is even.

    Args:
        digit: An integer digit (0-9).

    Returns:
        True if the digit is even, False otherwise.
    """
    return digit % 2 == 0

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Input Validation: Ensure the input is an integer.
    # While the prompt implies an integer input, production code should verify types.
    if not isinstance(num, int):
        raise TypeError(f"Input must be an integer. Received: {type(num).__name__}")

    # Handle the sign: The parity of digits depends on the magnitude, 
    # not the sign of the number. We work with the absolute value.
    absolute_value = abs(num)

    # Initialize counters
    even_count = 0
    odd_count = 0

    # Special case for zero: 
    # If the input is 0, it is a single digit which is even.
    if absolute_value == 0:
        even_count = 1
        odd_count = 0
        return (even_count, odd_count)

    # Convert the absolute value to a string to iterate over each digit.
    # This handles each digit independently regardless of its position.
    number_string = str(absolute_value)

    for char in number_string:
        # Convert the character back to an integer.
        # Since we derived this from str(abs(int)), it is guaranteed to be a digit.
        digit = int(char)

        # Check parity and increment the respective counter.
        if _is_even(digit):
            even_count += 1
        else:
            odd_count += 1

    # Return the results as a tuple in the specified order: (even, odd).
    return (even_count, odd_count)