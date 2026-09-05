from typing import List, Optional, Union

def first_even(numbers: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """
    Finds the first even number in a given list of numbers.

    An even number is defined as an integer that is divisible by 2 with no 
    remainder (n % 2 == 0). Non-integer floats that are mathematically 
    even (like 4.0) are considered even, while numbers with fractional 
    parts (like 4.5) are not even.

    Args:
        numbers: A list of integers or floats.

    Returns:
        The first even number found in the list, or None if no even 
        number exists or if the input list is empty.

    Raises:
        TypeError: If the input is not a list.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list explicitly
    if len(numbers) == 0:
        return None

    def is_even_number(value: Union[int, float]) -> bool:
        """
        Helper function to determine if a value is an even number.
        """
        # Check if the value is a numeric type
        if not isinstance(value, (int, float)):
            return False

        # Even numbers must be integers (e.g., 4.0 is even, 4.5 is not)
        # We check if the float is equal to its integer conversion
        if value != int(value):
            return False

        # A number is even if the remainder when divided by 2 is 0
        remainder = value % 2
        return remainder == 0

    # Iterate through the list to find the first occurrence
    for item in numbers:
        # Defensive check: Ensure we are working with valid numeric types
        if not isinstance(item, (int, float)):
            # We skip non-numeric types or could raise an error.
            # Based on production standards, skipping/ignoring is safer 
            # unless strict validation is required.
            continue

        if is_even_number(item):
            # Return immediately upon finding the first match
            return item

    # If the loop finishes without returning, no even number was found
    return None

if __name__ == "__main__":
    # The assertions provided in the problem description
    assert first_even([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert first_even([2, 3, 4]) == 2
    assert first_even([5, 6, 7]) == 6

    # Additional edge cases handled by the implementation
    assert first_even([]) is None
    assert first_even([1, 3, 5]) is None
    assert first_even([0]) == 0
    assert first_even([-2, -3, -4]) == -2
    assert first_even([4.0, 3.0]) == 4.0
    assert first_even([1.1, 2.2, 4.0]) == 4.0