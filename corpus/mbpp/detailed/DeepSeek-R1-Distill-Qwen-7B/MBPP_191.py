def check_monthnumber(month_name):
    """
    Check if the given month name corresponds to a month with 30 days.
    """
    # List of month names with 30 days (all lowercase)
    thirty_day_months = ['april', 'june', 'september', 'november']

    # Normalize the input to lowercase to handle case insensitivity
    normalized_month = month_name.lower()

    # Check if the normalized month is in the list of thirty-day months
    return normalized_month in thirty_day_months