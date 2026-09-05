def count(text, char):
    # Validate input: char must be a single character string
    if not isinstance(char, str) or len(char) != 1:
        return 0

    # Validate input: text must be a string
    if not isinstance(text, str):
        return 0

    # Initialize the counter
    count = 0

    # Iterate through each character in the text
    for c in text:
        if c == char:
            count += 1

    # Return the total count
    return count

# Example test cases:
# assert count("abcc", "c") == 2
# assert count("ababca", "a") == 3
# assert count("mnmm0pm", "m") == 4