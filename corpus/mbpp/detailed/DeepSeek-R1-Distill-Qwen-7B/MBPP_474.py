def replace_char(string, old_char, new_char):
    # Handle case where the replacement or old character is an empty string
    if not old_char or not new_char:
        return "Invalid input"

    # Convert the string to a list for easier manipulation
    chars = list(string)

    # Iterate over each character in the list
    for i in range(len(chars)):
        if chars[i] == old_char:
            chars[i] = new_char

    # Join the list back into a string and return it
    return ''.join(chars)