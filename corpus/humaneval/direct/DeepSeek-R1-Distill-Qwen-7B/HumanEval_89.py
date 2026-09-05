def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places."""
    shifted = []
    for i, c in enumerate(s):
        # Calculate the new character after shifting
        shift = 2 * i
        new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        shifted.append(new_char)
    return ''.join(shifted)