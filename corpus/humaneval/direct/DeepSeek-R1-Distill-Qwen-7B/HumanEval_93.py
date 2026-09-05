def encode(message):
    """
    Write a function that takes a message, and encodes it by swapping the case of all letters,
    replacing vowels with the letter two places ahead in the alphabet.

    Args:
        message: The input string to encode.

    Returns:
        The encoded string.
    """
    result = []
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    shift = 2

    for char in message:
        if char in vowels:
            # Replace the vowel with the one two places ahead
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result.append(new_char)
        else:
            # Swap the case
            if char.isupper():
                new_char = char.lower()
            else:
                new_char = char.upper()
            result.append(new_char)

    return ''.join(result)