import hashlib
from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Validate input type: Ensure the input is strictly a string.
    # Production-grade code should explicitly handle type mismatches.
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, received {type(text).__name__}")

    # Handle the specific edge case for empty strings as requested.
    if text == "":
        return None

    # Step 1: Encode the string into bytes.
    # MD5 functions operate on bytes, not high-level Unicode strings.
    # UTF-8 is the standard encoding for this operation.
    encoded_bytes: bytes = text.encode('utf-8')

    # Step 2: Initialize the MD5 hash object.
    hash_object = hashlib.md5()

    # Step 3: Update the hash object with the encoded bytes.
    hash_object.update(encoded_bytes)

    # Step 4: Get the hexadecimal representation of the digest.
    # hexdigest() returns a string of 32 hex digits.
    md5_hex_digest: str = hash_object.hexdigest()

    return md5_hex_digest

# Example usage (internal check):
# if __name__ == "__main__":
#     print(string_to_md5('Hello world'))  # Expected: 3e25960a79dbc69b674cd4ec67a72c62
#     print(string_to_md5(''))              # Expected: None