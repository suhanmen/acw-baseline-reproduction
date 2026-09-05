from typing import List

def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    A year is a leap year if it is divisible by 4, 
    except for years divisible by 100, unless they are also divisible by 400.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def calculate_odd_days_in_year(year: int) -> int:
    """
    Calculates the number of 'odd days' in a given year.
    In the context of the provided test cases, the 'odd days' calculation 
    follows the logic of calculating the remainder of total days in a year 
    divided by 7, adjusted for leap years.

    Logic derived from assertions:
    - 100: 365 days (non-leap). 365 % 7 = 1. Wait, assertion says 5.
    - 50: 365 days (non-leap). 365 % 7 = 1. Assertion says 6.
    - 75: 365 days (non-leap). 365 % 7 = 1. Assertion says 2.

    Re-evaluating the pattern from assertions:
    odd_Days(100) == 5
    odd_Days(50) == 6
    odd_Days(75) == 2

    Let's check (Year % 100) or similar.
    100 % 100 = 0 (doesn't match 5)
    100 % 7 = 2 (doesn't match 5)

    Wait, the standard definition of "Odd Days" in a period is the number of days 
    remaining after dividing the total number of days by 7.
    For a year:
    Non-leap year = 365 days = 52 weeks and 1 day. Odd days = 1.
    Leap year = 366 days = 52 weeks and 2 days. Odd days = 2.

    However, the provided assertions are:
    odd_Days(100) == 5
    odd_Days(50) == 6
    odd_Days(75) == 2

    Let's look for a different mathematical relationship:
    100: 100 % 10 = 0? No. 100 // 20? No.
    Let's try (Year % 10):
    100 % 10 = 0. Target 5.
    50 % 10 = 0. Target 6.
    75 % 10 = 5. Target 2.

    Let's try (Year % 12):
    100 % 12 = 4. Target 5.
    50 % 12 = 2. Target 6.
    75 % 12 = 3. Target 2.

    Let's try a simple calculation based on the input itself:
    100 -> 5. (Maybe 100 / 20?)
    50 -> 6. (Maybe 50 / 8?)
    75 -> 2.

    Wait, let's look at the standard "Odd Days" from the beginning of the era (e.g. AD 1):
    Odd days for year Y = (Number of years passed * 1) + (Number of leap years passed).
    This is the formula for odd days from 0001 to Year Y.
    Let's check:
    For Year 100:
    Leap years = 100 // 4 - 100 // 100 + 100 // 400 = 25 - 1 + 0 = 24.
    Total days = 100 * 365 + 24 = 36500 + 24 = 36524.
    36524 % 7 = 5. (Matches assertion!)

    For Year 50:
    Leap years = 50 // 4 - 50 // 100 + 50 // 400 = 12 - 0 + 0 = 12.
    Total days = 50 * 365 + 12 = 18250 + 12 = 18262.
    18262 % 7 = 6. (Matches assertion!)

    For Year 75:
    Leap years = 75 // 4 - 75 // 100 + 75 // 400 = 18 - 0 + 0 = 18.
    Total days = 75 * 365 + 18 = 27375 + 18 = 27393.
    27393 % 7 = 2. (Matches assertion!)

    The logic is: Calculate total odd days from Year 1 to Year Y.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if year < 1:
        # Handling non-positive years; usually calendar calculations start at 1.
        # If year is 0 or negative, we return 0 as a default for out of range.
        return 0

    # Calculation of leap years from 1 to 'year'
    # A year is leap if divisible by 4, but not 100, unless divisible by 400.
    # This formula calculates the number of leap years in the range [1, year].

    count_div_by_4 = year // 4
    count_div_by_100 = year // 100
    count_div_by_400 = year // 400

    total_leap_years = count_div_by_4 - count_div_by_100 + count_div_by_400

    # Total number of days from 0001 to Year 'year'
    # Every year has at least 365 days.
    days_from_common_years = year * 365
    total_days = days_from_common_years + total_leap_years

    # Odd days are the remainder when total days are divided by 7.
    odd_days = total_days % 7

    return odd_days

def odd_Days(year: int) -> int:
    """
    Wrapper function to match the required signature.
    """
    # Basic input validation
    if not isinstance(year, int):
        raise TypeError(f"Expected integer for year, got {type(year).__name__}")

    # Explicitly handle the logic
    result = calculate_odd_days_in_year(year)
    return result