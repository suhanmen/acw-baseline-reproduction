import re

def is_decimal(s: str) -> bool:
    """
    Checks if the given string is a decimal number with a precision of exactly 2.
    A decimal with precision of 2 means there are exactly two digits after the decimal point.
    """
    # Regex explanation:
    # ^          : Start of string
    # \d+        : One or more digits (integer part)
    # \.         : A literal dot
    # \d{2}      : Exactly two digits (fractional part)
    # $          : End of string
    pattern = r'^\d+\.\d{2}$'
    return bool(re.match(pattern, s))

if __name__ == "__main__":
    assert is_decimal('123.11') == True
    assert is_decimal('0.21') == True
    assert is_decimal('123.1214') == False