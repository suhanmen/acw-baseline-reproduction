from __future__ import annotations

from typing import Final

def _validate_month_name(month: str) -> str:
    """
    Validate that the provided month name is a non-empty string.

    Returns:
        The lower-cased version of the month name if valid.

    Raises:
        ValueError: If the month name is empty or contains invalid characters (non-alphabetic).
    """
    if not isinstance(month, str):
        raise TypeError(f"Month must be a string, got {type(month).__name__}")

    if not month:
        raise ValueError("Month name cannot be an empty string.")

    # Normalize to lowercase for comparison and processing
    normalized_month = month.lower()

    if not normalized_month.isalpha():
        raise ValueError(f"Month name '{month}' contains non-alphabetic characters.")

    return normalized_month

def _validate_day_number(day: int) -> int:
    """
    Validate that the provided day is a positive integer within the valid range for the month.

    Returns:
        The validated day number as an integer.

    Raises:
        TypeError: If the day is not an integer or is a boolean.
        ValueError: If the day is less than 1 or greater than 31.
    """
    # Explicit check for boolean before integer check, as bool is subclass of int in Python
    if isinstance(day, bool):
        raise TypeError("Day cannot be a boolean.")

    if not isinstance(day, int):
        raise TypeError(f"Day must be an integer, got {type(day).__name__}")

    if day < 1:
        raise ValueError(f"Day must be at least 1, got {day}.")

    if day > 31:
        raise ValueError(f"Day must be at most 31, got {day}.")

    return day

def _get_max_days_in_month(month_name: str) -> int:
    """
    Determine the maximum number of days in a given month.

    For this specific problem, we assume a non-leap year context for February
    unless the logic requires specific leap year handling for astronomical seasons.
    However, since the problem examples do not trigger February edge cases and
    seasons are generally treated as calendar blocks, we use standard month lengths.
    Note: Astronomical seasons might not align perfectly with calendar months,
    but the problem implies standard calendar-based season determination.

    Args:
        month_name: Validated month name (lowercase).

    Returns:
        Maximum days in the specified month.

    Raises:
        ValueError: If the month is invalid (not recognized).
    """
    month_to_max_days: Final[dict[str, int]] = {
        'january': 31,
        'february': 28,  # Simplified: ignoring leap years for standard season logic unless specified
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31,
    }

    if month_name not in month_to_max_days:
        raise ValueError(f"Invalid month name: {month_name}. Valid months are: {', '.join(sorted(month_to_max_days.keys()))}")

    return month_to_max_days[month_name]

def _determine_season(month: str, day: int) -> str:
    """
    Determine the season based on the month and day.

    Seasons are typically defined by date ranges. Different cultures may use
    different definitions, but the standard astronomical/calendar approximation
    is used here:
    - Winter: December 22 - March 20 (approx)
    - Spring: March 21 - June 20 (approx)
    - Summer: June 21 - September 22 (approx)
    - Autumn: September 23 - December 21 (approx)

    However, looking at the test cases:
    ('January', 4) -> winter
    ('October', 28) -> autumn
    ('June', 6) -> spring

    This suggests a simplified calendar-based approach where:
    - Winter: Jan, Feb, Mar (partial) OR Dec, Jan, Feb.
    Let's analyze the specific boundaries implied by common simplified logic:

    Standard simplified calendar logic often used in programming problems:
    - Spring: March, April, May
    - Summer: June, July, August
    - Autumn: September, October, November
    - Winter: December, January, February

    BUT the test case ('June', 6) -> spring contradicts the "June = Summer" logic.
    And ('January', 4) -> winter fits "Jan = Winter".
    And ('October', 28) -> autumn fits "Oct = Autumn".

    Re-evaluating based on the 'June' -> Spring assertion:
    This implies a hemisphere or specific range logic.
    If June is Spring, then:
    Spring likely starts early March and goes until late May/early June.
    Or perhaps the problem implies a specific range:

    Let's try a date-range approach aligned with the assertions:
    1. 'January', 4 -> winter.
    2. 'October', 28 -> autumn.
    3. 'June', 6 -> spring.

    Hypothesis: The seasons are divided by specific day-of-year thresholds or month ranges.
    If June 6 is Spring, then Spring must extend into June.
    If January 4 is Winter, Winter must cover January.
    If October 28 is Autumn, Autumn must cover October.

    Common Astronomical Seasons (Northern Hemisphere):
    - Winter: Dec 21 - Mar 20
    - Spring: Mar 21 - Jun 20
    - Summer: Jun 21 - Sep 22
    - Autumn: Sep 23 - Dec 21

    Check assertions against Astronomical:
    1. Jan 4 -> Dec 21 to Mar 20 (Winter). MATCH.
    2. Oct 28 -> Sep 23 to Dec 21 (Autumn). MATCH.
    3. June 6 -> Mar 21 to Jun 20 (Spring). MATCH.

    Conclusion: Use Northern Hemisphere Astronomical Season boundaries.

    Args:
        month: Validated month name (lowercase).
        day: Validated day number.

    Returns:
        The name of the season ('winter', 'spring', 'summer', or 'autumn').

    Raises:
        ValueError: If no season can be determined (though mathematically impossible with valid inputs).
    """
    # Convert month name to month number (1-12) for easier day-of-year calculation
    month_names: Final[dict[str, str]] = {
        'january': '1', 'february': '2', 'march': '3', 'april': '4',
        'may': '5', 'june': '6', 'july': '7', 'august': '8',
        'september': '9', 'october': '10', 'november': '11', 'december': '12'
    }

    if month not in month_names:
        # This should ideally be caught by _get_max_days_in_month, but added for safety
        raise ValueError(f"Unknown month: {month}")

    current_month_num = month_names[month]
    current_month_num_int = int(current_month_num)

    # Calculate day of year (DOY) assuming a non-leap year (365 days)
    # Cumulative days at start of each month:
    days_before_month: Final[dict[str, int]] = {
        '1': 0,    # January
        '2': 31,   # February
        '3': 59,   # March (31+28)
        '4': 90,   # April (31+28+31)
        '5': 120,  # May (31+28+31+30)
        '6': 151,  # June (31+28+31+30+31)
        '7': 181,  # July (31+28+31+30+31+30)
        '8': 212,  # August (31+28+31+30+31+30+31)
        '9': 243,  # September (31+28+31+30+31+30+31+31)
        '10': 273, # October (31+28+31+30+31+30+31+31+30)
        '11': 304, # November (31+28+31+30+31+30+31+31+30+31)
        '12': 334, # December (31+28+31+30+31+30+31+31+30+31+30)
    }

    start_of_current_month = days_before_month[current_month_num]
    day_of_year = start_of_current_month + day

    # Define Season Boundaries (Day of Year) for Northern Hemisphere
    # Winter: 0 to 80 (Dec 22 approx is DOY 356 or 0/365, Mar 20 is DOY 78)
    # Let's use precise DOY values based on Equinoxes/Solstices:
    # Winter Solstice: ~Dec 21 (DOY 355) -> Spring starts ~Mar 20 (DOY 78)
    # Spring Equinox: ~Mar 20 (DOY 78) -> Summer starts ~Jun 21 (DOY 172)
    # Summer Solstice: ~Jun 21 (DOY 172) -> Autumn starts ~Sep 22 (DOY 265)
    # Autumn Equinox: ~Sep 22 (DOY 265) -> Winter starts ~Dec 21 (DOY 355)

    # Adjusted ranges based on the specific assertions to ensure robustness:
    # Assertion: Jan 4 (DOY 4) -> Winter.
    # Assertion: Oct 28 (DOY 301: 273+28) -> Autumn.
    # Assertion: June 6 (DOY 156: 151+6) -> Spring.

    # If June 6 is Spring, then Spring must end after DOY 156.
    # Astronomical Spring ends Jun 20 (DOY 171). So 156 is within Spring.
    # If Oct 28 is Autumn, it must be after Autumn start (Sep 22, DOY 264) and before Winter (Dec 21, DOY 355).
    # 301 is within [265, 355].
    # If Jan 4 is Winter, it must be before Spring start (Mar 20, DOY 78) or after Winter start (Dec 21).
    # Since it's Jan, DOY is 4. Range for Winter: [0, 78) U (355, 365].

    # Refined Boundaries:
    WINTER_START: Final[int] = 356 # Dec 22 (inclusive)
    SPRING_START: Final[int] = 79  # Mar 21 (inclusive)
    SUMMER_START: Final[int] = 172 # Jun 21 (inclusive)
    AUTUMN_START: Final[int] = 265 # Sep 22 (inclusive)

    # Check for Winter
    # Winter covers early Jan (1-78) and late Dec (356-365)
    is_winter = (day_of_year >= WINTER_START and day_of_year <= 365) or \
                (day_of_year > 0 and day_of_year < SPRING_START)

    if is_winter:
        return 'winter'

    # Check for Spring
    # Spring covers Mar 21 (79) to Jun 20 (171)
    if SPRING_START <= day_of_year < SUMMER_START:
        return 'spring'

    # Check for Summer
    # Summer covers Jun 21 (172) to Sep 21 (264)
    if SUMMER_START <= day_of_year < AUTUMN_START:
        return 'summer'

    # Check for Autumn
    # Autumn covers Sep 22 (265) to Dec 20 (355)
    if AUTUMN_START <= day_of_year < WINTER_START:
        return 'autumn'

    # Fallback (should not be reached with valid logic)
    raise RuntimeError("Internal error: Could not determine season.")

def month_season(month: str,