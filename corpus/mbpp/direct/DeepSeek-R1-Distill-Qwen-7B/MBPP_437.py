def remove_odd(s):
    # Convert the string into a list of characters for easier manipulation
    chars = list(s)
    # Iterate over each character with their indices
    for i in range(len(chars)):
        # Check if the current character is present at an odd index
        if i % 2 == 1:
            # Remove the character at the odd index
            del chars[i]
    # Convert the list of characters back into a string
    return ''.join(chars)