def count_unset_bits(n: int) -> int:
    """
    Counts the number of unset bits (0s) in the binary representation 
    of a given integer, considering only the bits up to the most 
    significant bit.
    """
    if n == 0:
        return 1

    # Find the number of bits required to represent the number
    num_bits = n.bit_length()

    # Count the number of set bits (1s)
    set_bits = bin(n).count('1')

    # The number of unset bits is the difference between total bits
    # and set bits.
    return num_bits - set_bits