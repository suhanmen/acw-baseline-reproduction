import re
from typing import Optional

# --- Helper Function to Validate a Single Number Component (Day/Month) ---
def _validate_number_component(value_str: str, min_value: int, max_value: int, min_length: int, max_length: int) -> bool:
    """
    Validates if a string represents a valid number component for a date (day or month).

    Checks:
    1. Length matches the required range (e.g., single digit '1' is invalid, '01' is valid).
    2. Numeric content.
    3. Value falls within the allowed range [min_value, max_value].

    Args:
        value_str: The string to validate.
        min_value: The minimum integer value allowed.
        max_value: The maximum integer value allowed.
        min_length: The minimum required character length.
        max_length: The maximum required character length.

    Returns:
        True if valid, False otherwise.
    """
    # Check length constraints explicitly
    if len(value_str) != min_length:
        return False

    # Ensure no leading zeros unless the number itself is zero (though 00+ is usually invalid in dates)
    # For standard dates, '0' alone is invalid, '01'-'31' are valid. '00' is invalid.
    if len(value_str) > 1 and value_str.startswith('0'):
        return False

    try:
        int_value = int(value_str)
    except ValueError:
        return False

    if int_value < min_value or int_value > max_value:
        return False

    return True

# --- Helper Function to Validate Full Date String Structure and Values ---
def _validate_date_structure(date_str: str) -> bool:
    """
    Performs a preliminary structural check on the date string before regex parsing.

    Expected format: YYYY-MM-DD
    - 4 digits for year
    - '-' separator
    - 2 digits for month
    - '-' separator
    - 2 digits for day

    Args:
        date_str: The input string to validate.

    Returns:
        True if the structure is correct, False otherwise.
    """
    if date_str is None:
        return False

    if not isinstance(date_str, str):
        return False

    if len(date_str) != 10:
        return False

    if date_str[4] != '-' or date_str[2] != '-':
        return False

    if not date_str[0].isdigit() or not date_str[1].isdigit() or not date_str[3].isdigit():
        return False
    if not date_str[5].isdigit() or not date_str[6].isdigit():
        return False
    if not date_str[7].isdigit() or not date_str[8].isdigit():
        return False

    return True

# --- Helper Function to Parse Year ---
def _parse_year(date_str: str) -> Optional[int]:
    """
    Extracts and validates the year component from the date string.

    Args:
        date_str: The date string (YYYY-MM-DD).

    Returns:
        The integer year if valid, None otherwise.
    """
    year_str = date_str[0:4]

    if _validate_number_component(year_str, 0, 9999, 4, 4):
        return int(year_str)
    return None

# --- Helper Function to Parse Month ---
def _parse_month(date_str: str) -> Optional[int]:
    """
    Extracts and validates the month component from the date string.
    Valid months: 01 to 12.

    Args:
        date_str: The date string (YYYY-MM-DD).

    Returns:
        The integer month if valid, None otherwise.
    """
    month_str = date_str[5:7]

    if _validate_number_component(month_str, 1, 12, 2, 2):
        return int(month_str)
    return None

# --- Helper Function to Parse Day ---
def _parse_day(date_str: str) -> Optional[int]:
    """
    Extracts and validates the day component from the date string.
    Valid days: 01 to 31.

    Args:
        date_str: The date string (YYYY-MM-DD).

    Returns:
        The integer day if valid, None otherwise.
    """
    day_str = date_str[8:10]

    if _validate_number_component(day_str, 1, 31, 2, 2):
        return int(day_str)
    return None

# --- Main Function to Convert Date Format ---
def change_date_format(date_string: str) -> str:
    """
    Converts a date string from 'YYYY-MM-DD' format to 'DD-MM-YYYY' format.

    This function performs rigorous validation:
    1. Checks for None or non-string inputs.
    2. Checks for the correct length and separator positions.
    3. Uses regex to ensure digits only exist in the correct slots.
    4. Parses year, month, and day as integers.
    5. Validates the ranges for month (1-12) and day (1-31).
    6. Reconstructs the string in the new format.

    Args:
        date_string: A string in the format 'YYYY-MM-DD'.

    Returns:
        A string in the format 'DD-MM-YYYY'.

    Raises:
        ValueError: If the input string is not a valid date according to the rules.
    """

    # Step 1: Basic Type and Null Check
    if date_string is None:
        raise ValueError("Input date cannot be None.")

    if not isinstance(date_string, str):
        raise ValueError(f"Input date must be a string, but received {type(date_string).__name__}.")

    # Step 2: Structure Validation (Length and Separators)
    if len(date_string) != 10:
        raise ValueError(f"Invalid date length: expected 10 characters, found {len(date_string)}.")

    expected_sep_1 = 4
    expected_sep_2 = 7

    if date_string[expected_sep_1] != '-':
        raise ValueError("Invalid separator 1: expected '-' at index 4.")

    if date_string[expected_sep_2] != '-':
        raise ValueError("Invalid separator 2: expected '-' at index 7.")

    # Step 3: Regex Validation
    # Pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
    # We use regex to strictly enforce that ONLY digits and the specific separators are present.
    regex_pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    regex_match = re.match(regex_pattern, date_string)

    if not regex_match:
        # Although the length and separator checks above cover most cases,
        # regex ensures no non-digit characters slipped through in the number positions.
        # Example rejection: "2020-A1-13", "2020-0-13", "2020-1-3"
        raise ValueError("Invalid date format: expected digits in all number positions.")

    # Step 4: Parse Individual Components
    year = _parse_year(date_string)
    if year is None:
        raise ValueError("Invalid year component.")

    month = _parse_month(date_string)
    if month is None:
        raise ValueError("Invalid month component.")

    day = _parse_day(date_string)
    if day is None:
        raise ValueError("Invalid day component.")

    # Step 5: Formatting Logic
    # Convert integers back to strings with zero-padding for month and day
    formatted_day = str(day).zfill(2)
    formatted_month = str(month).zfill(2)
    formatted_year = str(year)

    # Step 6: Construct Result
    result_date = f"{formatted_day}-{formatted_month}-{formatted_year}"

    return result_date