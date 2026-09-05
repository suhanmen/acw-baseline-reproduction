def encode(message):
    """
    Write a function that takes a message and encodes it by swapping the case of all letters
    and replacing each vowel with the letter two places ahead in the English alphabet.
    """
    # Helper function to determine if a character is a vowel
    def is_vowel(char):
        return char.lower() in {'a', 'e', 'i', 'o', 'u'}

    # Helper function to shift a character two places ahead in the alphabet
    def shift_vowel(char):
        if not is_vowel(char):
            return char
        # Calculate new position, wrapping around if necessary
        base = ord('a') if char.islower() else ord('A')
        shifted = chr((ord(char) - base + 2) % 26 + base)
        return shifted

    # Check if the message is a string
    if not isinstance(message, str):
        return message

    # Process each character in the message
    encoded = []
    for char in message:
        # Swap case
        swapped = char.lower() if char.isupper() else char.upper()
        # Replace vowels
        if is_vowel(swapped):
            encoded_char = shift_vowel(swapped)
        else:
            encoded_char = swapped
        encoded.append(encoded_char)

    return ''.join(encoded)