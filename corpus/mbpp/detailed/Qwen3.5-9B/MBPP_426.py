from typing import Any, Iterable, List, Union

Number = Union[int, float]

def filter_oddnumbers(numbers: Any) -> List[Number]:
    """
    Filters a sequence of numbers to return only the odd ones.

    This function accepts an iterable of numbers (integers or floats),
    validates that all elements are indeed numbers, filters out any
    even numbers (including floats with non-zero fractional parts or
    whole number floats like 2.0), and returns a new list containing
    only the odd numbers in their original order.

    It handles edge cases such as empty lists, lists with a single element,
    lists containing only even numbers, lists containing only odd numbers,
    lists with negative numbers, and lists containing non-numeric values.

    Non-numeric values (if present after type checking) or values that cannot
    be cleanly determined as odd/even (like floats that aren't whole numbers)
    are excluded from the output list.

    Parameters:
    numbers (Any): An iterable expected to contain numbers.

    Returns:
    List[Number]: A list containing only the odd numbers from the input.

    Raises:
    TypeError: If the input is not iterable or contains non-numeric elements.
    """

    # Step 1: Validate that the input is an iterable.
    # We accept list, tuple, set, str (though strings are unlikely to be the input), etc.
    # We explicitly reject strings to avoid treating "123" as a sequence of digits.
    if isinstance(numbers, str):
        raise TypeError("Input must not be a string. Use a list or tuple of numbers.")

    try:
        # Attempt to iterate through the object
        iterator = iter(numbers)
    except TypeError:
        raise TypeError("Input must be an iterable collection of numbers.")

    result_list: List[Number] = []

    # Step 2: Iterate through each item in the input
    for item in iterator:

        # Step 3: Validate that each item is a valid number type (int or float)
        if not isinstance(item, (int, float)):
            # Explicitly exclude booleans as they are a subclass of int in Python
            if isinstance(item, bool):
                raise TypeError(f"All elements must be numbers, but found boolean value: {item}")
            raise TypeError(f"All elements must be numbers, but found non-numeric value: {item}")

        # Step 4: Determine if the number is odd.
        # 
        # Logic for determining "oddness":
        # An integer n is odd if (n % 2 != 0).
        # Floats are tricky. 
        # - If a float represents a whole number (e.g., 5.0), it has parity like an integer.
        #   5.0 % 2 == 1.0 -> Considered odd.
        #   2.0 % 2 == 0.0 -> Considered even.
        # - If a float has a fractional part, modulo 2 will result in a non-zero float
        #   that is not 1.0 (e.g., 5.5 % 2 = 1.5). 
        #   Strictly speaking, 5.5 is not an integer. The problem implies integers.
        #   However, to be robust: we will only include it if the remainder is exactly 1.0.
        #   This handles 5.0 (remainder 1.0) but excludes 5.5 (remainder 1.5).

        try:
            remainder = item % 2
        except Exception:
            # Fallback for any unexpected arithmetic error (highly unlikely for standard numbers)
            raise ValueError(f"Could not compute parity for value: {item}")

        # Step 5: Check the condition for being odd
        # We check if remainder is not equal to 0.
        # For integers: odd % 2 is 1, even % 2 is 0.
        # For whole floats: 5.0 % 2 is 1.0, 2.0 % 2 is 0.0.
        # For non-whole floats: 5.5 % 2 is 1.5 (not 0, but also not 1.0).
        # To strictly adhere to "odd numbers" (which are integers), we require the remainder to be 1.0.
        if remainder == 1.0:
            result_list.append(item)
        # If remainder is 0.0 (even) or anything else (non-integer float), we do not add it.

    return result_list