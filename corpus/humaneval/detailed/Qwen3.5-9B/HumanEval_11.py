from typing import List, Optional


def _validate_binary_string(s: str) -> None:
    """
    Validate that the input string is non-empty and contains only '0' and '1'.

    If validation fails, raises a ValueError with a descriptive message.

    Args:
        s (str): The string to validate.

    Raises:
        ValueError: If the string is empty or contains invalid characters.
    """
    if not s:
        raise ValueError(f"Input string must not be empty. Received empty string.")

    valid_characters = {'0', '1'}
    for char_index, char in enumerate(s):
        if char not in valid_characters:
            raise ValueError(
                f"Input string contains invalid character '{char}' at index {char_index}. "
                f"Expected only '0' or '1'."
            )


def _validate_equal_lengths(a: str, b: str) -> None:
    """
    Validate that both input strings have the same length.

    If validation fails, raises a ValueError with a descriptive message.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Raises:
        ValueError: If the lengths of the strings are not equal.
    """
    len_a = len(a)
    len_b = len(b)

    if len_a != len_b:
        raise ValueError(
            f"Input strings must have equal lengths. "
            f"Received lengths: a={len_a}, b={len_b}."
        )


def _compute_xor_pair(a_char: str, b_char: str) -> str:
    """
    Compute the XOR result for a single pair of binary characters.

    Logic:
    - If both are '0', result is '0'.
    - If both are '1', result is '0'.
    - If one is '0' and the other is '1', result is '1'.

    Args:
        a_char (str): Character from the first string ('0' or '1').
        b_char (str): Character from the second string ('0' or '1').

    Returns:
        str: The result of the XOR operation ('0' or '1').
    """
    if a_char == '0' and b_char == '0':
        return '0'
    elif a_char == '1' and b_char == '1':
        return '0'
    else:
        # This covers ('0', '1') and ('1', '0')
        return '1'


def _process_strings(a: str, b: str) -> str:
    """
    Perform the XOR operation on two validated binary strings of equal length.

    This function iterates through each character pair, computes the XOR,
    and accumulates the result into a new string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The resulting binary string after XOR operation.
    """
    result_chars: List[str] = []

    length = len(a)

    for index in range(length):
        char_a = a[index]
        char_b = b[index]
        xor_result = _compute_xor_pair(char_a, char_b)
        result_chars.append(xor_result)

    return ''.join(result_chars)


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    >>> string_xor('010', '110')
    '100'
    """
    _validate_binary_string(a)
    _validate_binary_string(b)

    _validate_equal_lengths(a, b)

    return _process_strings(a, b)