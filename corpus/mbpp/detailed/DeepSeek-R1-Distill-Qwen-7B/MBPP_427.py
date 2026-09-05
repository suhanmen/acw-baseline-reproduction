import re

def change_date_format(date_str):
    # Validate and extract date components using regex
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_str)
    if not match:
        return 'Invalid input'

    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

    # Check if month and day are valid
    try:
        month_int = int(month)
        day_int = int(day)
        if 1 <= month_int <= 12 and 1 <= day_int <= 31:
            pass
        else:
            return 'Invalid input'
    except ValueError:
        return 'Invalid input'

    # Ensure leading zeros for month and day
    formatted_month = f"{month_int:02d}"
    formatted_day = f"{day_int:02d}"

    # Combine into the desired format
    return f"{formatted_day}-{formatted_month}-{year}"