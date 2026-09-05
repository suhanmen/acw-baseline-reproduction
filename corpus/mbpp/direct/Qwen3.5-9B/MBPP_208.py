import re

def is_decimal(s):
    pattern = r'^-?\d+\.\d{2}$'
    return bool(re.match(pattern, s))