import re

def is_allowed_specific_char(input_string: str) -> bool:
    """
    Checks if the given string contains only alphanumeric characters (a-z, A-Z, 0-9)
    using regular expressions.
    """
    # ^ asserts the start of the string
    # [a-zA-Z0-9]* matches any number of alphanumeric characters
    # $ asserts the end of the string
    pattern = r'^[a-zA-Z0-9]*$'

    if re.match(pattern, input_string):
        return True
    else:
        return False

if __name__ == "__main__":
    assert is_allowed_specific_char("ABCDEFabcdef123450") == True
    assert is_allowed_specific_char("*&%@#!}{") == False
    assert is_allowed_specific_char("HELLOhowareyou98765") == True