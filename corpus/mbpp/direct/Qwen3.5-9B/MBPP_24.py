def binary_to_decimal(binary_str: str) -> int:
    """
    Convert a binary string (composed of '0' and '1') to its decimal equivalent.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        int: The decimal equivalent of the binary number.
    """
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a valid binary string (containing only '0' and '1').")

    return int(binary_str, 2)