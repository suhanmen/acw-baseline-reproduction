import re
from typing import Final

def change_date_format(date_string: str) -> str:
    """
    Converts a date string from 'yyyy-mm-dd' format to 'dd-mm-yyyy' 
    format using regular expressions.

    Args:
        date_string (str): The date string in yyyy-mm-dd format.

    Returns:
        str: The date string in dd-mm-yyyy format.

    Raises:
        ValueError: If the input string does not match the required format.
        TypeError: If the input is not a string.
    """

    # 1. Validate input type
    if not isinstance(date_string, str):
        raise TypeError(f"Input must be a string, received {type(date_string).__name__}")

    # 2. Handle empty input explicitly
    if not date_string.strip():
        raise ValueError("Input string cannot be empty or whitespace only.")

    # 3. Define the Regex pattern
    # ^ and $ ensure we match the entire string (no leading/trailing junk)
    # (\d{4}) captures 4 digits for the year
    # (\d{2}) captures 2 digits for the month
    # (\d{2}) captures 2 digits for the day
    # The hyphens are literal separators
    date_pattern: Final[str] = r"^(\d{4})-(\d{2})-(\d{2})$"

    # 4. Perform the regex match
    match = re.match(date_pattern, date_string)

    if match is None:
        raise ValueError(
            f"Invalid date format: '{date_string}'. "
            "Expected format is yyyy-mm-dd (e.g., 2026-01-02)."
        )

    # 5. Extract the captured groups
    # group(1) = year, group(2) = month, group(3) = day
    year_part: str = match.group(1)
    month_part: str = match.group(2)
    day_part: str = match.group(3)

    # 6. Construct the new format
    # We join the day, month, and year with hyphens
    # Since the regex captured fixed lengths, we don't need additional padding.
    formatted_date: str = f"{day_part}-{month_part}-{year_part}"

    return formatted_date

if __name__ == "__main__":
    # Testing the logic with provided assertions
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'