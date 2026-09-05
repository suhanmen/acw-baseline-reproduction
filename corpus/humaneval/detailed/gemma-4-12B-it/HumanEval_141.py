import string

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

    # Defensive check: Ensure the input is a string
    if not isinstance(file_name, str):
        return "No"

    # Condition 1: There should not be more than three digits ('0'-'9')
    digits_count = 0
    for char in file_name:
        if char.isdigit():
            digits_count += 1

    if digits_count > 3:
        return "No"

    # Condition 2: The file's name contains exactly one dot '.'
    dot_count = file_name.count('.')
    if dot_count != 1:
        return "No"

    # Split the string into name and extension based on the single dot
    # Since we know there is exactly one dot, we can use split
    parts = file_name.split('.')
    name_part = parts[0]
    extension_part = parts[1]

    # Condition 3: Substring before the dot should not be empty 
    # and it starts with a letter from the latin alphabet
    if name_part == "":
        return "No"

    first_char = name_part[0]
    is_latin_letter = False
    for letter in string.ascii_letters:
        if first_char == letter:
            is_latin_letter = True
            break

    if not is_latin_letter:
        return "No"

    # Condition 4: The substring after the dot should be one of: ['txt', 'exe', 'dll']
    valid_extensions = ["txt", "exe", "dll"]
    if extension_part not in valid_extensions:
        return "No"

    # If all checks pass
    return "Yes"