import re

def match(s: str) -> str:
    """
    Finds sequences of one upper case letter followed by lower case letters
    in the given string using regex.
    """
    # The pattern [A-Z][a-z]+ matches an uppercase letter followed 
    # by one or more lowercase letters.
    pattern = r'[A-Z][a-z]+'

    if re.search(pattern, s):
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    assert match("Geeks") == 'Yes'
    assert match("geeksforGeeks") == 'Yes'
    assert match("geeks") == 'No'