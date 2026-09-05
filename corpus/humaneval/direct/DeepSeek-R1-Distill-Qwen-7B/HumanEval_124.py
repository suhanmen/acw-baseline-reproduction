def valid_date(date):
    import re

    # Check if the date string matches the required format
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    # Split the date into month, day, year
    month_str, day_str, year_str = date.split('-')
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)

    # Check month validity
    if month < 1 or month > 12:
        return False

    # List of days for each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    # Check day validity for each month
    if day < 1:
        return False
    if day > month_days[month - 1]:
        return False

    # Check if it is a leap year
    def is_leap(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        else:
            return year % 400 == 0

    if month == 2:
        if is_leap(year):
            max_day = 29
        else:
            max_day = 28

    # If it is February, check against max_day
    if month == 2:
        if day > max_day:
            return False

    # All checks passed
    return True