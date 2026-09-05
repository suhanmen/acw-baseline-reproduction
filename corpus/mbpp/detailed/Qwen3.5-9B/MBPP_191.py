def check_monthnumber(month_name: str) -> bool:
    """
    Determines if the given month name corresponds to a month with 30 days.

    This function validates the input, normalizes the month name to handle
    case sensitivity, checks for valid month names, and returns True if the
    month has exactly 30 days, False otherwise.

    Args:
        month_name: A string representing the name of a month (e.g., "January").

    Returns:
        True if the month has 30 days, False otherwise (including invalid months).

    Valid months with 30 days: April, June, September, November.
    """

    # Define a set of valid month names for quick lookup and validation
    valid_months = {
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    }

    # Define the mapping of valid month names to their day counts
    month_day_counts = {
        "january": 31,
        "february": 28,  # Standard year; leap year exception handled by returning False for 30 check anyway
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }

    # Normalize the input string to lowercase for case-insensitive comparison
    normalized_month = month_name.lower()

    # Validate that the input is a non-empty string
    if not isinstance(month_name, str):
        return False

    if not normalized_month:
        return False

    # Check if the normalized month name exists in our set of valid months
    if normalized_month not in valid_months:
        return False

    # Retrieve the number of days for the validated month
    days_in_month = month_day_counts[normalized_month]

    # Check if the retrieved day count is exactly 30
    has_thirty_days = (days_in_month == 30)

    return has_thirty_days