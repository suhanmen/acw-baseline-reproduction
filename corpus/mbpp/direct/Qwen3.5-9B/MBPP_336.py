def check_monthnum(month_name: str) -> bool:
    """
    Returns True if the given month name contains only 28 days (February in non-leap years).
    Returns False otherwise.
    """
    return month_name.lower() == "february"