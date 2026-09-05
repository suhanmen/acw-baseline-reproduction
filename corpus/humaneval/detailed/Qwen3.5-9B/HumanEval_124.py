import re
from datetime import datetime

def _is_empty_string(date: str) -> bool:
    """Check if the provided date string is empty."""
    return date == ""

def _has_invalid_characters(date: str) -> bool:
    """
    Check if the date string contains any character other than digits and hyphens.
    This ensures the format is strictly mm-dd-yyyy and not mm/dd/yyyy or similar.
    """
    if not date:
        return True
    # The set of allowed characters is digits (0-9) and hyphen (-)
    for char in date:
        if not (char.isdigit() or char == '-'):
            return True
    return False

def _count_hyphens(date: str) -> int:
    """Count the number of hyphens in the date string."""
    return date.count('-')

def _check_hyphen_count(date: str) -> bool:
    """
    The format mm-dd-yyyy requires exactly two hyphens.
    Any other count (0, 1, 3, etc.) indicates an invalid format.
    """
    return _count_hyphens(date) == 2

def _split_date_components(date: str) -> tuple:
    """
    Split the date string by hyphens into month, day, and year parts.
    Returns a tuple of (month_str, day_str, year_str) if successful,
    or None if the split fails (e.g., if hyphen count was wrong).
    """
    if _count_hyphens(date) != 2:
        return None
    parts = date.split('-')
    if len(parts) != 3:
        return None
    return (parts[0], parts[1], parts[2])

def _parse_component(component_str: str) -> int:
    """
    Attempt to parse a component string into an integer.
    Returns None if the string contains non-digit characters or is empty.
    """
    if not component_str or not component_str.isdigit():
        return None
    return int(component_str)

def _validate_month_string(month_str: str) -> bool:
    """
    Validate the month string:
    1. Must consist only of digits.
    2. Must not be empty.
    3. Must be between 1 and 12 inclusive.
    """
    if not month_str:
        return False
    if not month_str.isdigit():
        return False

    try:
        month = int(month_str)
        if month < 1 or month > 12:
            return False
        return True
    except ValueError:
        return False

def _validate_day_string(day_str: str) -> bool:
    """
    Validate the day string:
    1. Must consist only of digits.
    2. Must not be empty.
    3. Must be between 1 and 31 inclusive (we check max 31 first, 
       then specific month rules later).
    """
    if not day_str:
        return False
    if not day_str.isdigit():
        return False

    try:
        day = int(day_str)
        if day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

def _validate_year_string(year_str: str) -> bool:
    """
    Validate the year string:
    1. Must consist only of digits.
    2. Must not be empty.
    Note: There are no explicit range constraints given for the year in the problem 
    statement, so we only check that it's a non-empty digit string.
    """
    if not year_str:
        return False
    if not year_str.isdigit():
        return False
    return True

def _validate_day_range_for_month(day: int, month: int) -> bool:
    """
    Apply specific day limits based on the month:
    - Months 1, 3, 5, 7, 8, 10, 12: Max 31 days
    - Months 4, 6, 9, 11: Max 30 days
    - Month 2: Max 29 days (as per problem statement, ignoring leap year logic 
      since the problem explicitly states "not higher than 29" for month 2)
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= day <= 31
    elif month in (4, 6, 9, 11):
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 29
    else:
        # Should never reach here if _validate_month_string passed
        return False

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    # Rule 1: The date string is not empty.
    if _is_empty_string(date):
        return False

    # Check for invalid characters (Rule 4 implication: only digits and hyphens allowed)
    if _has_invalid_characters(date):
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    # This implies exactly two hyphens.
    if not _check_hyphen_count(date):
        return False

    # Split the date into components
    components = _split_date_components(date)
    if components is None:
        return False

    month_str, day_str, year_str = components

    # Parse and validate each component
    # Validate Month
    if not _validate_month_string(month_str):
        return False
    month = int(month_str)

    # Validate Day
    if not _validate_day_string(day_str):
        return False
    day = int(day_str)

    # Validate Year
    if not _validate_year_string(year_str):
        return False

    # Rule 2: Validate day ranges based on month
    # Re-verify day is >= 1 (already done in _validate_day_string)
    # and check upper bounds per month
    if not _validate_day_range_for_month(day, month):
        return False

    return True