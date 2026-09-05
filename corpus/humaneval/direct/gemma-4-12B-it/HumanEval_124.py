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
    if not date:
        return False

    # Check format mm-dd-yyyy (exactly 10 characters)
    # Length check and dash placement
    parts = date.split('-')
    if len(parts) != 3:
        return False

    mm_str, dd_str, yyyy_str = parts

    if len(mm_str) != 2 or len(dd_str) != 2 or len(yyyy_str) != 4:
        return False

    # Ensure all parts are numeric
    if not (mm_str.isdigit() and dd_str.isdigit() and yyyy_str.isdigit()):
        return False

    month = int(mm_str)
    day = int(dd_str)
    year = int(yyyy_str)

    # Rule 3: Month validation
    if month < 1 or month > 12:
        return False

    # Rule 2: Day validation based on month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False

    return True