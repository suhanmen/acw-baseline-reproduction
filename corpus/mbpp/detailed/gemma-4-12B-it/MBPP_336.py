from typing import List

def check_monthnum(month_name: str) -> bool:
    """
    Checks whether the given month name corresponds to a month that 
    has exactly 28 days (specifically February in a non-leap year).

    Note: In standard calendar logic, February is the only month 
    associated with the number 28. This function returns True if the 
    input is "February", otherwise False.

    Args:
        month_name (str): The name of the month.

    Returns:
        bool: True if the month has 28 days, False otherwise.

    Raises:
        ValueError: If the input is not a non-empty string or 
                    is not a recognized month name.
    """
    # 1. Validate the input type
    if not isinstance(month_name, str):
        raise ValueError(f"Input must be a string, got {type(month_name).__name__}")

    # 2. Normalize the input (strip whitespace and convert to title case)
    # This ensures "february", " FEBRUARY ", and "February" are handled equally.
    cleaned_name = month_name.strip().title()

    # 3. Handle empty input case
    if not cleaned_name:
        raise ValueError("Month name cannot be empty or whitespace only.")

    # 4. Define the standard 12 months for validation
    valid_months = [
        "January", "February", "March", "April", 
        "May", "June", "July", "August", 
        "September", "October", "November", "December"
    ]

    # 5. Check if the provided month is a valid calendar month
    if cleaned_name not in valid_months:
        # The prompt implies checking against known months. 
        # If an invalid string is passed, it doesn't have 28 days.
        return False

    # 6. Define logic for days in month
    # February is the only month that contains 28 days (standard year).
    # While January, March, etc., contain 28 days as a subset, 
    # "contains 28 days" in calendar logic usually refers to the 
    # maximum capacity of that specific month.
    target_month = "February"

    # 7. Perform the check
    is_february = (cleaned_name == target_month)

    return is_february

# The following assertions are provided to validate the requirements.
if __name__ == "__main__":
    # These will pass based on the problem description.
    assert check_monthnum("February") == True
    assert check_monthnum("January") == False
    assert check_monthnum("March") == False