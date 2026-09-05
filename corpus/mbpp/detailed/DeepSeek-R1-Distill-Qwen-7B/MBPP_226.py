def odd_values_string(s):
    # Convert the string to a list for easier manipulation
    chars = list(s)
    # Initialize a list to collect characters at even indices
    result = []
    # Iterate over each character with its index
    for index in range(len(chars)):
        # Check if the index is even
        if index % 2 == 0:
            # Append the character to the result list
            result.append(chars[index])
    # Join the list into a string and return
    return ''.join(result)