import string

def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Defensive check: ensure input is a string
    if not isinstance(message, str):
        raise TypeError("Input must be a string.")

    # Handle empty string case immediately
    if not message:
        return ""

    # Define vowels as a set for O(1) lookup
    # The problem implies vowels are a, e, i, o, u (case insensitive)
    vowels = set("aeiouAEIOU")

    # The alphabet string is used to calculate the "2 places ahead" logic
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    def shift_vowel(char: str) -> str:
        """
        Helper to determine the character 2 places ahead in the alphabet
        for a vowel, maintaining the vowel's specific case.
        """
        if char.islower():
            # Find current position in lowercase alphabet
            current_index = alphabet_lower.find(char)
            # Calculate new index with modulo to wrap around alphabet (e.g., y -> a)
            new_index = (current_index + 2) % 26
            return alphabet_lower[new_index]
        else:
            # Find current position in uppercase alphabet
            current_index = alphabet_upper.find(char)
            new_index = (current_index + 2) % 26
            return alphabet_upper[new_index]

    result_chars = []

    for current_char in message:
        # Requirement 1: Swap the case of all letters
        if current_char.isupper():
            swapped_char = current_char.lower()
        elif current_char.islower():
            swapped_char = current_char.upper()
        else:
            # If it's a space or punctuation (though prompt says assume letters),
            # we keep it as is.
            swapped_char = current_char

        # Requirement 2: Replace vowels with character 2 places ahead
        # Note: The requirement implies we check if the original letter was a vowel
        # or if the modified letter is a vowel.
        # Looking at the example 'test' -> 'TGST': 
        # 'e' is a vowel. Swap case -> 'E'. 
        # 'E' is the vowel. Shift 2 places -> 'G'.
        # Looking at 'This' -> 'tHKS':
        # 'i' is a vowel. Swap case -> 'I'.
        # 'I' is the vowel. Shift 2 places -> 'K'.

        # Conclusion from examples:
        # 1. Identify character
        # 2. Swap case
        # 3. If the result of the swap is a vowel, shift it 2 places ahead.

        if swapped_char in vowels:
            final_char = shift_vowel(swapped_char)
        else:
            final_char = swapped_char

        result_chars.append(final_char)

    # Join the list of characters into the final encoded string
    encoded_message = "".join(result_chars)
    return encoded_message