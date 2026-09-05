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
    if '.' not in file_name:
        return 'No'

    dot_index = file_name.index('.')
    if file_name.count('.') != 1:
        return 'No'

    name_part = file_name[:dot_index]
    ext_part = file_name[dot_index + 1:]

    valid_extensions = ['txt', 'exe', 'dll']
    if ext_part not in valid_extensions:
        return 'No'

    if len(name_part) == 0:
        return 'No'

    if not name_part[0].isalpha():
        return 'No'

    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'

    return 'Yes'