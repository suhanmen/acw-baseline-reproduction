import re

def is_decimal(s):
    """
    Check if the given string is a valid decimal number with exactly two digits after the decimal point.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a valid decimal with exactly two decimal places, False otherwise.
    """
    # Regular expression pattern to match a valid decimal with exactly two decimal places
    pattern = r'^(\d+|\d*\.\d{2})$'

    # Check if the string matches the pattern
    if re.fullmatch(pattern, s):
        # Extract the integer and decimal parts
        match = re.match(pattern, s)
        integer_part = match.group(1)
        decimal_part = match.group(2)

        # Check if the integer part is valid (can be empty or start with zero)
        if integer_part and not integer_part.isdigit():
            return False
        # Check if the decimal part has exactly two digits
        if not decimal_part or not decimal_part.isdigit() or len(decimal_part) != 2:
            return False
        # All checks passed
        return True
    else:
        return False

# Test cases
assert is_decimal('123.11') == True, "Test case 1 failed"
assert is_decimal('0.21') == True, "Test case 2 failed"
assert is_decimal('123.1214') == False, "Test case 3 failed"
assert is_decimal('.') == False, "Test case 4 failed"
assert is_decimal('123') == False, "Test case 5 failed"
assert is_decimal('123.') == False, "Test case 6 failed"
assert is_decimal('00.25') == True, "Test case 7 failed"
assert is_decimal('0123.45') == True, "Test case 8 failed"
assert is_decimal('-123.45') == False, "Test case 9 failed"
print("All test cases passed successfully")