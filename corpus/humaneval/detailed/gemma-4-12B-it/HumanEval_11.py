from typing import List


def _validate_binary_string(s: str) -> None:
    """
    Validates that the input string consists only of '0' and '1'.
    Raises ValueError if invalid characters are found.
    """
    allowed_chars = {'0', '1'}
    for char in s:
        if char not in allowed_chars:
            raise ValueError(f"Invalid character '{char}' found. Strings must only contain '0' and '1'.")


def _get_xor_bit(bit_a: str, bit_b: str) -> str:
    """
    Performs XOR on two single-character binary strings.
    Returns '1' if the bits are different, '0' if they are the same.
    """
    # Convert characters to integers for calculation
    int_a = int(bit_a)
    int_b = int(bit_b)

    # Perform XOR logic
    xor_result = int_a ^ int_b

    # Return result as string
    return str(xor_result)


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check for null inputs or non-string types if necessary, 
    # though type hints suggest they are strings.
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    # Validate that both strings contain only '0' and '1'
    _validate_binary_string(a)
    _validate_binary_string(b)

    # Handle the case where lengths are different
    # If the problem implies they should be equal, we handle it here.
    # If it implies padding, the logic would change. 
    # Based on the standard XOR string problem, we assume equal lengths.
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length.")

    # Handle empty strings (degenerate case)
    if len(a) == 0:
        return ""

    # Prepare a list to store the resulting bits
    result_bits: List[str] = []

    # Iterate through the characters of both strings simultaneously
    for i in range(len(a)):
        char_a = a[i]
        char_b = b[i]

        # Compute the XOR of the current pair of bits
        xor_bit = _get_xor_bit(char_a, char_b)

        # Append the result to our list
        result_bits.append(xor_bit)

    # Join the list of bits back into a single string
    final_result = "".join(result_bits)

    return final_result