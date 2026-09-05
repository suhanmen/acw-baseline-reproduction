def check_monthnum(month_name):
    """
    Check if the given month name contains 28 days.

    Args:
        month_name (str): A string representing the name of a month.

    Returns:
        bool: True if the month name contains '28', False otherwise.

    Raises:
        ValueError: If the input is not a valid month name.

    Examples:
        >>> check_monthnum("February")
        True  # February has 28 days (29 in a leap year)
        >>> check_monthnum("January")
        False  # January has 31 days
        >>> check_monthnum("March")
        False  # March has 31 days
        >>> check_monthnum("")
        False  # Empty string is invalid
        >>> check_monthnum("invalid_month")
        False  # Invalid month name results in False
    """
    # Step 1: Validate the input
    valid_months = {
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    }

    if not isinstance(month_name, str):
        raise ValueError("Invalid input: month_name must be a string.")

    if month_name not in valid_months:
        return False

    # Step 2: Check if the month name contains '28'
    return "28" in month_name