from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Validate each character in 'a'
    for char in a:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid character '{char}' in string a")
    # Validate each character in 'b'
    for char in b:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid character '{char}' in string b")
    # Check if the lengths are the same
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")

    # Perform XOR operation on each corresponding bit
    result = []
    for i in range(len(a)):
        a_bit = int(a[i])
        b_bit = int(b[i])
        result.append(str(a_bit ^ b_bit))

    return ''.join(result)