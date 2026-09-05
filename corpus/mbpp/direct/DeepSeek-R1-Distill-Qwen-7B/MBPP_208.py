python
import re

def is_decimal(s):
    """
    Check if a string represents a decimal number with exactly 2 decimal places.
    """
    pattern = r"^(\d+)\.(\d{2})$"
    return bool(re.match(pattern, s))