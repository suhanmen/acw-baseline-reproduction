import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == "":
        return None

    # Encode the string to bytes, then compute the md5 hash
    hash_object = hashlib.md5(text.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()