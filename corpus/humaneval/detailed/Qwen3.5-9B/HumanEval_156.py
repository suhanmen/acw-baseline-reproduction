from typing import Union, Tuple, Optional

# Define constants for Roman numeral conversion mapping in descending order.
# Each entry maps a value to its corresponding Roman numeral symbol.
# This order ensures greedy subtraction logic works correctly (e.g., 400 -> "CD", not "CD" vs "CDD").
ROMAN_VALUES: Tuple[Tuple[int, str], ...] = (
    (1000, "m"),
    (900, "cm"),
    (500, "d"),
    (400, "cd"),
    (100, "c"),
    (90, "xc"),
    (50, "l"),
    (40, "xl"),
    (10, "x"),
    (9, "ix"),
    (5, "v"),
    (4, "iv"),
    (1, "i"),
)

def _validate_input(value: Union[int, float, str, None]) -> int:
    """
    Validates the input value and returns the integer if valid.

    Constraints:
    1. The input must not be None.
    2. The input must be an integer type (not float, even if whole).
    3. The input must be greater than 0.
    4. The input must be less than or equal to 1000.

    Raises:
        TypeError: If the input is not an integer or is None.
        ValueError: If the input is out of the range [1, 1000].
    """
    if value is None:
        raise TypeError("Input value cannot be None.")

    # Ensure the type is exactly int. Floating point numbers like 150.0 are rejected.
    if not isinstance(value, int):
        raise TypeError(f"Expected an integer, got {type(value).__name__}.")

    if value <= 0:
        raise ValueError(f"Input must be a positive integer (>= 1), got {value}.")

    if value > 1000:
        raise ValueError(f"Input must be <= 1000, got {value}.")

    return value

def _convert_number_to_roman(num: int) -> str:
    """
    Converts a validated positive integer (1-1000) into its Roman numeral string representation.
    Uses the greedy approach with the predefined ROMAN_VALUES mapping.

    Algorithm:
    1. Iterate through the mapping of values from largest to smallest.
    2. For each value, determine how many times it fits into the remaining number.
    3. Append the corresponding symbol that many times to the result string.
    4. Subtract the total value from the number.
    5. Continue until the number is reduced to 0.
    """
    result_parts: list[str] = []
    remaining_value: int = num

    for value, symbol in ROMAN_VALUES:
        # Calculate how many times the current 'value' fits into 'remaining_value'
        if remaining_value >= value:
            count = remaining_value // value
            if count > 0:
                # Append the symbol 'count' times
                symbol_repeated = symbol * count
                result_parts.append(symbol_repeated)
                # Update the remaining value
                remaining_value = remaining_value - (value * count)

        # Safety check: if remaining value is 0, we can stop early
        if remaining_value == 0:
            break

    # Join the list of string parts to form the final Roman numeral string
    final_string = "".join(result_parts)

    return final_string

def int_to_mini_roman(number: Union[int, float, str, None]) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.

    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Step 1: Validate the input strictly.
    validated_number: int = _validate_input(number)

    # Step 2: Perform the conversion using the helper function.
    # The helper function ensures the logic is explicit and handles the conversion.
    roman_uppercase: str = _convert_number_to_roman(validated_number)

    # Step 3: Ensure the output is lowercase (though our mapping is already lowercase,
    # this step acts as a defensive conversion for consistency).
    final_output: str = roman_uppercase.lower()

    return final_output