from typing import Union

def validate_month_number(month_number: Union[int, float]) -> int:
    """
    Validates that the input is a non-negative integer between 1 and 12 inclusive.

    Args:
        month_number: The input value to validate.

    Returns:
        The validated month number as an integer.

    Raises:
        TypeError: If the input is not an integer (excluding booleans which are a subclass of int).
        ValueError: If the input is outside the range of 1 to 12.
    """
    # Explicitly reject booleans before checking for int, as bool is a subclass of int in Python
    if isinstance(month_number, bool):
        raise TypeError("Month number must not be a boolean.")

    if not isinstance(month_number, int):
        raise TypeError(f"Month number must be an integer, got {type(month_number).__name__}.")

    if month_number < 1 or month_number > 12:
        raise ValueError(f"Month number must be between 1 and 12, got {month_number}.")

    return month_number

def _days_in_month(month_number: int) -> int:
    """
    Helper function to determine the number of days in a specific month.

    Args:
        month_number: The month number (1-12).

    Returns:
        The number of days in the specified month.
    """
    # Define the number of days for each month explicitly
    # Month 1: Jan (31), 2: Feb (28/29), 3: Mar (31), 4: Apr (30), 
    # 5: May (31), 6: Jun (30), 7: Jul (31), 8: Aug (31), 
    # 9: Sep (30), 10: Oct (31), 11: Nov (30), 12: Dec (31)

    if month_number == 2:
        return 28  # We only care about 31 days vs others per problem context, 
                   # but strictly Feb is not 31. Leap year logic not needed 
                   # for the specific condition of "contains 31 days".
    elif month_number in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month_number in (4, 6, 9, 11):
        return 30
    else:
        # This part should theoretically be unreachable if validation is correct,
        # but acts as a fallback for unexpected states.
        return 0

def check_monthnumb_number(month_number: Union[int, float]) -> bool:
    """
    Checks whether the given month number contains 31 days.

    Args:
        month_number: The month number to check. Must be an integer between 1 and 12.

    Returns:
        True if the month has 31 days, False otherwise.

    Raises:
        TypeError: If the input is not a valid integer (excluding booleans).
        ValueError: If the month number is not between 1 and 12.
    """
    # Step 1: Validate the input explicitly
    validated_month = validate_month_number(month_number)

    # Step 2: Determine the number of days in the validated month
    days_count = _days_in_month(validated_month)

    # Step 3: Check if the count equals 31
    has_thirty_one_days = days_count == 31

    return has_thirty_one_days