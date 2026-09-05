import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts
    parts = file_name.split('.', 1)
    if len(parts) != 2:
        return 'No'

    # Check the part before the dot
    before_dot = parts[0]
    if not before_dot:
        return 'No'
    if not before_dot[0].isalpha():
        return 'No'

    # Check the part after the dot
    after_dot = parts[1]
    valid_extensions = ['txt', 'exe', 'dll']
    if after_dot not in valid_extensions:
        return 'No'

    # Check for more than three digits in the entire file name
    if re.search(r'\d{4,}', file_name):
        return 'No'

    # All conditions met
    return 'Yes'