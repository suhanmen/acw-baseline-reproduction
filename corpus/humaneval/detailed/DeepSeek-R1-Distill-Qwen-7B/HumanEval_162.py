import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert the input string into bytes using utf-8 encoding
    try:
        text_bytes = text.encode('utf-8')
    except AttributeError:
        # Handle the case where 'text' is not a string (though the function expects a string)
        return None

    # Compute the MD5 hash of the bytes
    md5_hash = hashlib.md5(text_bytes).hexdigest()

    return md5_hash