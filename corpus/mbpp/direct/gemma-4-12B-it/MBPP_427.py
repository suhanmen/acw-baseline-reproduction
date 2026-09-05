import re

def change_date_format(date_string: str) -> str:
    """
    Converts a date string from yyyy-mm-dd format to dd-mm-yyyy format using regex.
    """
    # Regex pattern to match yyyy, mm, and dd
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    # Replacement string to reorder the groups
    replacement = r"\3-\2-\1"

    return re.sub(pattern, replacement, date_string)

if __name__ == "__main__":
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'