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

    # Step 1: Validate input type and handle non-string inputs explicitly
    if not isinstance(file_name, str):
        return "No"

    # Step 2: Check for empty string or string with only whitespace that results in no meaningful content
    if file_name == "":
        return "No"

    # Step 3: Count the occurrences of the dot character
    dot_count = file_name.count(".")

    # Check condition: exactly one dot
    if dot_count != 1:
        return "No"

    # Step 4: Split the filename into name and extension based on the single dot
    dot_index = file_name.index(".")
    file_name_part = file_name[:dot_index]
    extension_part = file_name[dot_index + 1:]

    # Step 5: Validate that the substring before the dot is not empty
    if file_name_part == "":
        return "No"

    # Step 6: Validate that the substring before the dot starts with a latin alphabet letter
    first_char = file_name_part[0]
    if not ((first_char.isalpha()) and (first_char.isascii())):
        return "No"

    # Step 7: Check if the extension is one of the allowed types
    allowed_extensions = ["txt", "exe", "dll"]
    if extension_part not in allowed_extensions:
        return "No"

    # Step 8: Count the number of digits in the entire file name
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    # Check condition: not more than three digits
    if digit_count > 3:
        return "No"

    # All conditions have been met
    return "Yes"