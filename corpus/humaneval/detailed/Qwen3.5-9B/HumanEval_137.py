import re
from typing import Union, Optional

def _parse_number(value: Union[int, float, str]) -> float:
    """
    Parses an integer, float, or string representation of a number into a float.

    Handles:
    - Standard Python integers and floats.
    - Strings with '.' as decimal separator.
    - Strings with ',' as decimal separator (common in many locales).
    - Strings with mixed formats (e.g., "1,23" or "1.23").

    Raises:
        ValueError: If the input cannot be parsed as a number.
        TypeError: If the input type is not supported.
    """
    if isinstance(value, (int, float)):
        # Ensure we don't have a bool slipping in (bool is a subclass of int)
        if isinstance(value, bool):
            raise TypeError(f"Boolean values are not accepted: {value}")
        return float(value)

    if isinstance(value, str):
        s = value.strip()
        if not s:
            raise ValueError("Empty string cannot be parsed as a number.")

        # Check for comma as decimal separator
        if ',' in s and '.' not in s:
            # Replace comma with dot if it's the only decimal-like character
            # and ensure there's only one comma
            if s.count(',') == 1:
                s = s.replace(',', '.')
            else:
                raise ValueError(f"Invalid number format with multiple commas: {value}")

        # Validate that the string looks like a valid number before parsing
        # This regex matches optional sign, digits, optional decimal part
        pattern = r'^[+-]?(?:\d+\.?\d*|\.\d+)$'
        if not re.match(pattern, s):
            raise ValueError(f"Invalid number format: {value}")

        return float(s)

    raise TypeError(f"Unsupported type for number parsing: {type(value).__name__}")

def _normalize_value(value: Union[int, float, str]) -> Union[tuple, None]:
    """
    Normalizes a single input value into a tuple of (numeric_value, original_value).
    Returns None if the value is None (shouldn't happen based on caller, but safe to handle).
    """
    if value is None:
        return None

    parsed = _parse_number(value)
    return (parsed, value)

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Optional[Union[int, float, str]]:
    """
    Compares two values which can be integers, floats, or strings representing numbers.

    Rules:
    1. Converts both values to their numeric equivalents.
    2. If one is an int/float and the other is a string, returns the string if it's larger.
    3. If both are the same type (both strings or both numbers), returns the larger one in that type.
    4. If the numeric values are equal, returns None.
    5. If the string representations are identical (even if numeric values differ due to formatting like "1.0" vs "1"),
       we still compare numerically first. If numerically equal, return None.

    Note: The problem states "Return the larger variable in its given variable type".
    This implies:
    - If a > b numerically, return a in its original form.
    - If b > a numerically, return b in its original form.
    - If a == b numerically, return None.

    We do not mix types in the return value; we return the original type of the winner.
    """

    # Step 1: Validate inputs are not None (basic defensive check)
    if a is None or b is None:
        raise ValueError("Neither argument can be None.")

    # Step 2: Parse both values to their numeric representations
    # We catch specific errors to provide clear messages
    try:
        num_a, orig_a = _normalize_value(a)
        num_b, orig_b = _normalize_value(b)
    except (ValueError, TypeError) as e:
        raise e

    # Step 3: Compare numeric values
    # Using a small epsilon for float comparison to handle floating point inaccuracies
    # However, for most business logic, direct comparison or exact equality check is often intended.
    # Given the examples ("1", 1 -> None), strict numeric equality is expected.

    diff = num_a - num_b

    # Check for equality with a tolerance for floating point errors
    is_equal = abs(diff) < 1e-9

    if is_equal:
        # If numerically equal, return None as per requirements
        return None
    elif num_a > num_b:
        # 'a' is larger, return it in its original type
        return orig_a
    else:
        # 'b' is larger, return it in its original type
        return orig_b