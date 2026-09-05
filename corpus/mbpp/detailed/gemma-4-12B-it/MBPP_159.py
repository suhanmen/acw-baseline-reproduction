from typing import Tuple

def month_season(month: str, day: int) -> str:
    """
    Determines the season based on the provided month name and day of the month.

    The logic follows a standard transition:
    - Winter: December 1 to March 20
    - Spring: March 21 to June 20
    - Summer: June 21 to September 21
    - Autumn: September 22 to November 30

    Note: For the purpose of the provided assertions:
    - 'January', 4 -> 'winter'
    - 'October', 28 -> 'autumn'
    - 'June', 6 -> 'spring'

    Wait, looking at the provided assertions:
    - 'January', 4 -> 'winter'
    - 'October', 28 -> 'autumn'
    - 'June', 6 -> 'spring'

    Standard meteorological seasons:
    Winter: Dec, Jan, Feb
    Spring: Mar, Apr, May
    Summer: Jun, Jul, Aug
    Autumn: Sep, Oct, Nov

    Let's map based on common logic that satisfies the specific assertions provided:
    January -> winter
    October -> autumn
    June -> spring (Note: In some systems June 1-20 is spring, 21-30 is summer)

    To satisfy:
    1. (January, 4) -> winter
    2. (October, 28) -> autumn
    3. (June, 6) -> spring

    Logic implementation:
    - Winter: Dec, Jan, Feb
    - Spring: Mar, Apr, May, June (early)
    - Summer: June (late), Jul, Aug
    - Autumn: Sep, Oct, Nov
    """

    # --- Input Validation ---
    if not isinstance(month, str):
        raise ValueError("Month must be a string.")

    if not isinstance(day, int):
        raise ValueError("Day must be an integer.")

    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31.")

    # Normalize month string for comparison
    normalized_month = month.strip().capitalize()

    # Define month order for easy indexing
    months_list = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if normalized_month not in months_list:
        raise ValueError(f"Invalid month name: {month}. Expected one of {months_list}")

    # Get index (0 = January, 11 = December)
    month_index = months_list.index(normalized_month)

    # --- Season Determination Logic ---
    # Based on the specific requirements provided by the assertions:
    # June 6 is 'spring', so the transition from Spring to Summer must be after June 6.
    # Since June 21 is the standard meteorological start of Summer, we use that.

    # Define boundaries based on standard meteorological seasons:
    # Winter: Dec 1 to Mar 20
    # Spring: Mar 21 to Jun 20
    # Summer: Jun 21 to Sep 21
    # Autumn: Sep 22 to Nov 30

    is_winter = False
    is_spring = False
    is_summer = False
    is_autumn = False

    # Check Winter: Dec (Index 11) or Jan/Feb (Index 0, 1) or Mar (Index 2) <= 20
    if month_index == 11: # December
        is_winter = True
    elif month_index == 0: # January
        is_winter = True
    elif month_index == 1: # February
        is_winter = True
    elif month_index == 2 and day <= 20: # March
        is_winter = True

    # Check Spring: Mar (Index 2) > 20 or Apr/May (Index 3, 4) or June (Index 5) <= 20
    elif month_index == 2 and day > 20: # March
        is_spring = True
    elif month_index == 3: # April
        is_spring = True
    elif month_index == 4: # May
        is_spring = True
    elif month_index == 5 and day <= 20: # June
        is_spring = True

    # Check Summer: June (Index 5) > 20 or Jul/Aug (Index 6, 7) or Sep (Index 8) <= 21
    elif month_index == 5 and day > 20: # June
        is_summer = True
    elif month_index == 6: # July
        is_summer = True
    elif month_index == 7: # August
        is_summer = True
    elif month_index == 8 and day <= 21: # September
        is_summer = True

    # Check Autumn: Sep (Index 8) > 21 or Oct/Nov (Index 9, 10)
    elif month_index == 8 and day > 21: # September
        is_autumn = True
    elif month_index == 9: # October
        is_autumn = True
    elif month_index == 10: # November
        is_autumn = True

    # Final Assignment
    if is_winter:
        return "winter"
    elif is_spring:
        return "spring"
    elif is_summer:
        return "summer"
    elif is_autumn:
        return "autumn"
    else:
        # This part handles the overlap/gaps if logic is slightly off
        # In this specific flow, the elifs are mutually exclusive.
        # Defaulting to a fallback just in case.
        return "unknown"