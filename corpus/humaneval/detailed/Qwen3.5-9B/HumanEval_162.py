import hashlib
import os


def validate_text_input(text):
    """
    Validates that the input is a string and not empty.

    Returns:
        str: The validated text if it passes checks.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text is an empty string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, got {type(text).__name__}")

    if len(text) == 0:
        raise ValueError("Input string cannot be empty")

    return text


def hash_string_with_md5(text_bytes):
    """
    Computes the MD5 hash of the given bytes.

    Args:
        text_bytes (bytes): The byte representation of the string to hash.

    Returns:
        str: The hexadecimal representation of the MD5 hash.
    """
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(text_bytes)
    hex_digest = md5_hash_object.hexdigest()
    return hex_digest


def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    try:
        validated_text = validate_text_input(text)
    except (TypeError, ValueError):
        return None

    try:
        text_bytes = validated_text.encode('utf-8')
    except UnicodeEncodeError as encode_error:
        raise ValueError(f"Could not encode string to UTF-8: {encode_error}") from encode_error

    md5_hash_result = hash_string_with_md5(text_bytes)

    return md5_hash_result