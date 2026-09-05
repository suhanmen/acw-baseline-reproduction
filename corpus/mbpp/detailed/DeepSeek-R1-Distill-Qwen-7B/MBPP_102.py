def snake_to_camel(s):
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    if not s:
        return ""

    # Check for invalid characters
    if not s.isalnum():
        raise ValueError("String must contain only alphanumeric characters and underscores.")

    # Split the snake case string into words
    words = s.split('_')

    if len(words) == 1:
        return words[0]

    # Process the first word
    first_word = words[0].lower()

    # Process subsequent words
    camel_words = [first_word]
    for word in words[1:]:
        camel_word = word[0].upper() + word[1:].lower()
        camel_words.append(camel_word)

    # Join all words to form the camel case string
    return ''.join(camel_words)