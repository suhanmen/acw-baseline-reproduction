from typing import Union, List

class InputValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_positive_integer(value: Union[int, str, float, None]) -> int:
    """
    Validates that the input is a positive integer.

    Args:
        value: The value to validate.

    Returns:
        The validated integer.

    Raises:
        InputValidationError: If the value is not a positive integer.
    """
    if value is None:
        raise InputValidationError("Input cannot be None.")

    if isinstance(value, str):
        try:
            int_value = int(value)
        except ValueError:
            raise InputValidationError(f"Input '{value}' is not a valid integer string.")

        if '.' in value:
            raise InputValidationError(f"Input '{value}' contains a decimal point but represents an integer.")

    elif isinstance(value, float):
        if value != int(value):
            raise InputValidationError(f"Input '{value}' has a fractional part but must be an integer.")
        int_value = int(value)
    elif isinstance(value, bool):
        # In Python, bool is a subclass of int, but we explicitly reject booleans
        raise InputValidationError(f"Boolean values are not allowed as input.")
    elif isinstance(value, int):
        int_value = value
    else:
        raise InputValidationError(f"Unsupported type: {type(value).__name__}. Expected an integer.")

    if int_value <= 0:
        raise InputValidationError(f"Input must be a positive integer, got {int_value}.")

    return int_value

def get_first_digit(number: int) -> int:
    """
    Extracts the first digit of a positive integer.

    Args:
        number: A positive integer.

    Returns:
        The first digit of the number.
    """
    while number >= 10:
        number = number // 10
    return number

def get_last_digit(number: int) -> int:
    """
    Extracts the last digit of a positive integer.

    Args:
        number: A positive integer.

    Returns:
        The last digit of the number.
    """
    return number % 10

def count_n_digit_numbers_with_property(n: int, property_fn) -> int:
    """
    Counts how many n-digit numbers satisfy a given property.

    Since iterating through all n-digit numbers for large n is computationally
    infeasible, this function uses combinatorial logic based on the structure
    of n-digit numbers.

    An n-digit number ranges from 10^(n-1) to 10^n - 1.

    Args:
        n: The number of digits.
        property_fn: A function that takes an n-digit number and returns True if it satisfies the condition.

    Returns:
        The count of numbers satisfying the property.
    """
    if n == 1:
        # Special case for single-digit numbers (1-9)
        count = 0
        for i in range(1, 10):
            if property_fn(i):
                count += 1
        return count

    # For n > 1:
    # Total n-digit numbers = 9 * 10^(n-1)
    # First digit ranges from 1 to 9.
    # Last digit ranges from 0 to 9.

    count_starting_with_one = 0
    count_ending_with_one = 0
    count_starting_and_ending_with_one = 0

    # 1. Count numbers starting with 1
    # Format: 1 _ _ ... _
    # The first digit is fixed as 1.
    # The remaining (n-1) digits can be anything from 0-9.
    # Number of such integers = 10^(n-1)
    count_starting_with_one = 10 ** (n - 1)

    # 2. Count numbers ending with 1
    # Format: _ _ ... _ 1
    # The last digit is fixed as 1.
    # The first digit can be 1-9 (cannot be 0 for an n-digit number).
    # The middle (n-2) digits can be 0-9.
    # Number of such integers = 9 * 10^(n-2)
    if n > 1:
        count_ending_with_one = 9 * (10 ** (n - 2))
    else:
        count_ending_with_one = 0 # Handled by n=1 logic above if needed, but here n>1

    # 3. Count numbers starting AND ending with 1
    # Format: 1 _ ... _ 1
    # First digit is 1. Last digit is 1.
    # The middle (n-2) digits can be 0-9.
    if n > 1:
        count_starting_and_ending_with_one = 10 ** (n - 2)
    else:
        count_starting_and_ending_with_one = 0

    # Apply Inclusion-Exclusion Principle:
    # |A U B| = |A| + |B| - |A n B|
    # where A = starts with 1, B = ends with 1
    total_count = count_starting_with_one + count_ending_with_one - count_starting_and_ending_with_one

    return total_count

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    This function validates the input, handles edge cases (specifically n=1),
    and uses combinatorial logic to efficiently calculate the result without
    iterating through potentially trillions of numbers.

    Args:
        n: A positive integer representing the number of digits.

    Returns:
        The count of n-digit positive integers that start or end with the digit 1.

    Raises:
        InputValidationError: If n is not a valid positive integer.
    """
    # Step 1: Validate input
    validated_n = validate_positive_integer(n)

    # Step 2: Handle the specific edge case for single-digit numbers
    if validated_n == 1:
        # 1-digit numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9
        # Start with 1: {1} -> count 1
        # End with 1: {1} -> count 1
        # Start AND End with 1: {1} -> count 1
        # Union: {1} -> count 1
        # Alternatively, manually check:
        # Numbers are 1..9
        # Start with 1: 1
        # End with 1: 1
        # Both: 1
        # Result: 1 + 1 - 1 = 1
        return 1

    # Step 3: Calculate using combinatorial logic for n > 1
    # We do not need to call the generic counter with a lambda for performance,
    # as we have derived the explicit formulas above. We call the cleaner 
    # version that implements the logic directly for clarity and safety.

    # Count numbers starting with 1
    # Pattern: 1xxxx...x
    # Choices for remaining (n-1) digits: 10 options each (0-9)
    count_starts = 10 ** (validated_n - 1)

    # Count numbers ending with 1
    # Pattern: x...x1
    # First digit choices: 9 options (1-9)
    # Middle (n-2) digits: 10 options each (0-9)
    count_ends = 9 * (10 ** (validated_n - 2))

    # Count numbers starting AND ending with 1
    # Pattern: 1x...x1
    # Middle (n-2) digits: 10 options each (0-9)
    count_both = 10 ** (validated_n - 2)

    # Apply Inclusion-Exclusion Principle
    # |Starts OR Ends| = |Starts| + |Ends| - |Both|
    final_count = count_starts + count_ends - count_both

    return final_count