def char_frequency(string):
    # Initialize an empty dictionary to store character counts
    char_counts = {}

    # Convert the string into a list of characters
    characters = list(string)

    # Iterate over each character in the list
    for char in characters:
        # Update the count for the character, or add it if not present
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Format the counts into a dictionary with character keys
    return dict(char_counts)