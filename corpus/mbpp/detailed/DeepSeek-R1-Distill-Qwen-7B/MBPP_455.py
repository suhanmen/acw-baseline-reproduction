def check_monthnumb_number(month):
    # Check if the input is a valid month number
    if not isinstance(month, int) or month < 1 or month > 12:
        return False
    # List of months with 31 days
    thirty_one_days_months = {1, 3, 5, 7, 8, 10, 12}
    # Return True if the month is in the set, otherwise False
    return month in thirty_one_days_months