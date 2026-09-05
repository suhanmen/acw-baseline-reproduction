def month_season(month, day):
    """
    Determines the season based on the given month and day.

    Args:
        month (str): A three-letter abbreviation for the month.
        day (int): The day of the month.

    Returns:
        str: The season ('winter', 'autumn', 'spring', 'summer').

    Raises:
        ValueError: If the month is invalid or the day is out of range.
    """
    # Validate input
    if not isinstance(month, str) or len(month) != 3 or not month.isalpha():
        raise ValueError("Invalid month")
    if not isinstance(day, int) or day < 1:
        raise ValueError("Invalid day")

    # Get day of year
    day_of_year = get_day_of_year(month, day)
    return get_season(day_of_year)

def get_day_of_year(month, day, leap_year=False):
    """
    Converts a month and day into the day of the year.

    Args:
        month (str): Three-letter month abbreviation.
        day (int): The day of the month.
        leap_year (bool): Whether to consider a leap year for February.

    Returns:
        int: The day of the year.
    """
    month_days = {
        'jan': 31, 'feb': 28 if not leap_year else 29,
        'mar': 31, 'apr': 30, 'may': 31,
        'jun': 30, 'jul': 31, 'aug': 31,
        'sep': 30, 'oct': 31, 'nov': 30,
        'dec': 31
    }

    if month not in month_days:
        raise ValueError(f"Invalid month: {month}")
    if day < 1 or day > month_days[month]:
        raise ValueError(f"Invalid day for month: {month}")
    return sum(month_days[month_key] for month_key in month_days if month_key < month) + day

def get_season(day_of_year):
    """
    Determines the season based on the day of the year.

    Args:
        day_of_year (int): The day of the year.

    Returns:
        str: The season ('winter', 'autumn', 'spring', 'summer').
    """
    if day_of_year <= 10:
        return 'winter'
    elif day_of_year <= 51:
        return 'spring'
    elif day_of_year <= 92:
        return 'summer'
    elif day_of_year <= 122:
        return 'autumn'
    elif day_of_year <= 152:
        return 'winter'
    elif day_of_year <= 181:
        return 'spring'
    elif day_of_year <= 212:
        return 'summer'
    elif day_of_year <= 243:
        return 'autumn'
    else:
        return 'winter'