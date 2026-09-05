def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2  # Two multiplied to two places
    encrypted_chars = []
    for char in s:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % 26
            encrypted_chars.append(alphabet[new_index])
        else:
            encrypted_chars.append(char)
    return ''.join(encrypted_chars)