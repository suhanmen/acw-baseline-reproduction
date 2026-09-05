from typing import List

def check_monthnumber(month_name: str) -> bool:
    """
    Determines whether a given month name belongs to a month that has exactly 30 days.

    Args:
        month_name (str): The name of the month (e.g., "January", "February").

    Returns:
        bool: True if the month has 30 days, False otherwise.

    Raises:
        ValueError: If the input is not a valid month name or is not a string.
    """
    # Validate that the input is a string
    if not isinstance(month_name, str):
        raise ValueError(f"Input must be a string, received: {type(month_name)}")

    # Normalize the input for consistent comparison
    # This handles cases like "june", "JUNE", or " June "
    normalized_month = month_name.strip().capitalize()

    # Define the set of months that contain exactly 30 days
    # These are April, June, September, and November
    months_with_30_days: List[str] = [
        "April",
        "June",
        "September",
        "November"
    ]

    # List of all valid month names for comprehensive validation
    all_months: List[str] = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Validate that the input is a recognized month
    if normalized_month not in all_months:
        raise ValueError(f"'{month_name}' is not a valid month name.")

    # Check if the normalized month is in the 30-day list
    is_30_day_month: bool = normalized_month in months_with_30_days

    return is_30_day_month

# Explicitly checking the requirements via assertions as specified
if __name__ == "__main__":
    # These assertions are part of the problem requirements
    assert check_monthnumber("February") == False
    assert check_monthnumber("June") == True
    assert check_monthnumber("April") == True