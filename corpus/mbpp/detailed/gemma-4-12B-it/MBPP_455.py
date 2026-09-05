from typing import Any

def check_monthnumb_number(month_number: Any) -> bool:
    """
    Checks whether the given month number corresponds to a month 
    that has exactly 31 days.

    Args:
        month_number: The month number to check (expected to be an integer).

    Returns:
        bool: True if the month has 31 days, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not within the valid range of 1 to 12.
    """
    # Validate that the input is an integer
    if not isinstance(month_number, int):
        raise TypeError(f"Input must be an integer, received {type(month_number).__name__}")

    # Validate that the input is a valid month number (1-12)
    if month_number < 1 or month_number > 12:
        raise ValueError(f"Month number must be between 1 and 12, received {month_number}")

    # Define the set of months that contain 31 days
    # January = 1, March = 3, May = 5, July = 7, August = 8, October = 10, December = 12
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}

    # Check if the provided month number exists in our list of 31-day months
    is_31_day_month = month_number in months_with_31_days

    return is_31_day_month

if __name__ == "__main__":
    # Assertion checks as required by the problem description
    assert check_monthnumb_number(5) == True
    assert check_monthnumb_number(2) == False
    assert check_monthnumb_number(6) == False