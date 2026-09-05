from typing import Union, List

def validate_year(year: int) -> None:
    """
    Validates that the input is a valid year (positive integer).

    Args:
        year: The year to validate.

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year is not positive.
    """
    if not isinstance(year, int):
        raise TypeError(f"Year must be an integer, got {type(year).__name__}")
    if year <= 0:
        raise ValueError(f"Year must be positive, got {year}")

def is_leap_year(year: int) -> bool:
    """
    Determines if a year is a leap year based on the Gregorian calendar rules.

    Rules:
    1. If divisible by 400, it is a leap year.
    2. If divisible by 100 but not 400, it is NOT a leap year.
    3. If divisible by 4 but not 100, it is a leap year.
    4. Otherwise, it is not a leap year.

    Args:
        year: The year to check.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    is_divisible_by_400 = (year % 400 == 0)
    is_divisible_by_100 = (year % 100 == 0)
    is_divisible_by_4 = (year % 4 == 0)

    if is_divisible_by_400:
        return True
    if is_divisible_by_100:
        return False
    if is_divisible_by_4:
        return True

    return False

def get_days_in_year(year: int) -> int:
    """
    Returns the total number of days in a specific year.

    Args:
        year: The year to check.

    Returns:
        366 if it's a leap year, 365 otherwise.
    """
    return 366 if is_leap_year(year) else 365

def calculate_total_days(year: int) -> int:
    """
    Calculates the total number of days elapsed from year 1 up to and including the given year.

    This counts every single day in every year from year 1 to the given year.

    Args:
        year: The target year.

    Returns:
        Total count of days from year 1 to the target year inclusive.
    """
    total_days = 0

    # Handle single year case efficiently by avoiding a loop for 1000s of years
    # However, the problem implies calculating 'odd days' relative to the start of the calendar
    # (conceptually year 1, day 1).
    # We must iterate to sum up days for years 1 through 'year'.

    current_year = 1
    while current_year <= year:
        total_days += get_days_in_year(current_year)
        current_year += 1

    return total_days

def extract_odd_days_from_total(total_days: int) -> int:
    """
    Extracts the number of odd days from the total days count.

    An 'odd day' is defined as the remainder when total days are divided by 7.
    0 odd days = Sunday (or start of week equivalent)
    1 odd day = Monday
    ...

    Args:
        total_days: The total number of days accumulated.

    Returns:
        The remainder when total_days is divided by 7.
    """
    return total_days % 7

def odd_Days(year: int) -> int:
    """
    Calculates the number of odd days in a given year.

    This function calculates the cumulative total days from the start of the 
    calendar (Year 1) up to the end of the specified 'year', and then returns
    the remainder modulo 7.

    Note: The naming convention "odd_Days(year)" in this context interprets 'year' 
    as the *end* of the period for which we are counting days (cumulative from year 1).
    This matches the behavior required by the assertions:
      - Year 100: 100 years have passed.
      - Year 50: 50 years have passed.
      - Year 75: 75 years have passed.

    Args:
        year: The year up to which days are counted (inclusive).

    Returns:
        The number of odd days (remainder modulo 7).

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year is not positive.
    """
    # Step 1: Validate the input explicitly
    validate_year(year)

    # Step 2: Calculate total days from year 1 to the given year
    total_accumulated_days = calculate_total_days(year)

    # Step 3: Calculate the remainder modulo 7
    result = extract_odd_days_from_total(total_accumulated_days)

    return result