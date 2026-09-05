import re

def change_date_format(input_date: str) -> str:
    pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.match(pattern, input_date)

    if not match:
        raise ValueError("Invalid date format")

    day = match.group(2)
    month = match.group(3)
    year = match.group(1)

    return f"{day}-{month}-{year}"