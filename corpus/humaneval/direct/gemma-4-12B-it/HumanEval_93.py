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
    vowels = 'aeiouAEIOU'
    result = []

    for char in message:
        if char.isalpha():
            # Swap the case first
            swapped = char.swapcase()

            # Check if the original character was a vowel
            if char in vowels:
                # Find the position in alphabet
                # We need to find the character 2 places ahead of the vowel
                # The rule says "replaces all vowels... with the letter that appears 
                # 2 places ahead of that vowel". 
                # Note: The examples show 'i' (vowel) becomes 'K' (case swapped) 
                # and 'a' (vowel) becomes 'C' (case swapped).
                # Let's trace 'This': T->t, h->H, i->K, s->S. 
                # 'i' is the 9th letter. 9+2 = 11th letter (k). Swapped case = K.
                # 'a' is the 1st letter. 1+2 = 3rd letter (c). Swapped case = C.

                # To handle wrapping (e.g., 'y' though not a vowel), 
                # but for vowels, we just shift.
                base = ord('A') if swapped.isupper() else ord('a')
                # The shift is based on the alphabet position of the vowel.
                # vowel 'i' is 9th letter. 9+2 = 11th letter.
                # We calculate position relative to 'a' or 'A'

                # Identify if original was uppercase or lowercase to determine target
                is_upper = char.isupper()
                vowel_idx = ord(char.lower()) - ord('a')
                new_idx = (vowel_idx + 2) % 26
                new_char = chr(ord('a') + new_idx)

                # Apply swap case logic: 
                # If original was lowercase, result is uppercase.
                # If original was uppercase, result is lowercase.
                if is_upper:
                    result.append(new_char.upper())
                else:
                    result.append(new_char.lower())
            else:
                result.append(swapped)
        else:
            result.append(char)

    return "".join(result)

# Re-evaluating the logic based on the provided examples:
# 'test' -> 'TGST'
# t (lower) -> T (upper)
# e (vowel, lower) -> 5+2=7 (g), swap case -> G
# s (lower) -> S (upper)
# t (lower) -> T (upper)
# Result: TGST. Correct.

# 'This' -> 'tHKS'
# T (upper) -> t (lower)
# h (lower) -> H (upper)
# i (vowel, lower) -> 9+2=11 (k), swap case -> K
# s (lower) -> S (upper)
# Result: tHKS. Correct.

def encode(message):
    vowels = "aeiouAEIOU"
    res = ""
    for char in message:
        if char in vowels:
            # Find its position in alphabet (0-25)
            # and move 2 steps forward
            is_upper = char.isupper()
            pos = ord(char.lower()) - ord('a')
            new_pos = (pos + 2) % 26
            new_char = chr(ord('a') + new_pos)
            # Swap case relative to original
            if is_upper:
                res += new_char.lower()
            else:
                res += new_char.upper()
        elif char.isalpha():
            res += char.swapcase()
        else:
            res += char
    return res