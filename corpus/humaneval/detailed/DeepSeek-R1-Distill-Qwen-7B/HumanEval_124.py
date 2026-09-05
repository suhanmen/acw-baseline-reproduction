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
    def _is_valid_format(s):
        if len(s) != 10:
            return False
        if s[2] != '-' or s[5] != '-':
            return False
        try:
            return s[0:2].isdigit() and s[3:4].isdigit() and s[6:10].isdigit()
        except IndexError:
            return False

    def _is_valid_month(m):
        return 1 <= m <= 12

    def _is_valid_day(d, m, y):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= d <= 31
        elif m in [4, 6, 9, 11]:
            return 1 <= d <= 30
        elif m == 2:
            # Leap year check
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                return 1 <= d <= 29
            else:
                return 1 <= d <= 28
        else:
            return False

    # Check format first
    if not _is_valid_format(date):
        return False

    # Split the date
    try:
        m, d, y = map(int, date.split('-'))
    except ValueError:
        return False

    # Check month
    if not _is_valid_month(m):
        return False

    # Check day
    if not _is_valid_day(d, m, y):
        return False

    return True

# Example tests:
# valid_date('03-11-2000') => True
# valid_date('15-01-2012') => False
# valid_date('04-0-2040') => False
# valid_date('06-04-2020') => True
# valid_date('06/04/2020') => False