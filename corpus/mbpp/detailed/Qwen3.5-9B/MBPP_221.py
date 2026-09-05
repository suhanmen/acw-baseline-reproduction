from typing import List, Optional, Union

Number = Union[int, float]


def validate_input(numbers: List[Number]) -> List[Number]:
    """
    Validates that the input is a list and that all elements are numbers.
    Returns the validated list if successful.
    Raises a TypeError if validation fails.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but got {type(numbers).__name__}")

    for index, value in enumerate(numbers):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number (got {type(value).__name__})"
            )

    return numbers


def is_even(candidate: Number) -> bool:
    """
    Determines if a given number is even.

    An even number is an integer divisible by 2 with no remainder.
    This function handles both positive and negative integers, as well as floats
    that are effectively whole numbers divisible by 2 (though logically, 
    the concept of 'even' applies strictly to integers).

    Floats that are not whole numbers (e.g., 2.5) or odd floats are treated as not even.
    """
    # Check if the candidate is actually an integer type.
    # In Python, booleans are a subclass of int, so we must exclude them explicitly.
    if isinstance(candidate, bool):
        raise TypeError(f"Expected a number, but got a boolean at this position")

    if not isinstance(candidate, int):
        # If it's a float, it cannot be considered 'even' in the strict mathematical sense
        # usually required for such puzzles unless specified otherwise (e.g., 2.0 is even).
        # However, to be safe and strict about types matching 'numbers' in lists of integers:
        # We will treat non-integers as not even, but allow integers that happen to be 
        # the result of float math if the input was floats.
        # Given the problem examples use integers, let's be strict: 
        # Only integers are candidates for being 'even'.
        return False

    # Check divisibility by 2
    return candidate % 2 == 0


def find_first_even(numbers: List[Number]) -> Optional[Number]:
    """
    Finds the first even number in the given list.

    If no even number is found, returns None.

    Args:
        numbers: A list of numbers.

    Returns:
        The first even number found, or None if no even number exists.
    """
    # Explicitly handle the empty list case early
    if len(numbers) == 0:
        return None

    for index, number in enumerate(numbers):
        if is_even(number):
            return number

    # If the loop completes without returning, no even number was found
    return None


def first_even(numbers: List[Number]) -> Optional[Number]:
    """
    Main entry point to find the first even number in a list.

    This function wraps the logic with robust input validation.
    It ensures the input is a list of numbers before attempting to process it.

    Args:
        numbers: A list containing numerical values.

    Returns:
        The first even integer found in the list.
        Returns None if the list is empty or contains no even numbers.

    Raises:
        TypeError: If the input is not a list or if any element is not a number.
    """
    # Step 1: Validate the input structure and contents
    validated_numbers = validate_input(numbers)

    # Step 2: Search for the first even number
    result = find_first_even(validated_numbers)

    return result