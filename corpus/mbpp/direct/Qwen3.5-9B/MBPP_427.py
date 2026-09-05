import re

def change_date_format(date_str):
    """
    Converts a date string from yyyy-mm-dd format to dd-mm-yyyy format using regex.

    Args:
        date_str (str): Date string in yyyy-mm-dd format.

    Returns:
        str: Date string in dd-mm-yyyy format.
    """
    # Pattern to capture year, month, and day groups
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    match = re.match(pattern, date_str)

    if not match:
        raise ValueError("Invalid date format. Expected yyyy-mm-dd.")

    year, month, day = match.groups()
    return f"{day}-{month}-{year}"

# Verification of assertions
assert change_date_format("2026-01-02") == '02-01-2026'
assert change_date_format("2020-11-13") == '13-11-2020'
assert change_date_format("2021-04-26") == '26-04-2021'