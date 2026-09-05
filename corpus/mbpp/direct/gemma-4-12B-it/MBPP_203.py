def hamming_Distance(x: int, y: int) -> int:
    """
    Calculates the Hamming distance between two integers.
    The Hamming distance is the number of positions at which the 
    corresponding bits are different.
    """
    # XOR the two numbers to get a result where bits are set 
    # only if they are different in x and y.
    xor_result = x ^ y

    # Count the number of set bits (1s) in the XOR result.
    # bin() returns a string like '0b101', count('1') gives the distance.
    return bin(xor_result).count('1')

if __name__ == "__main__":
    assert hamming_Distance(4, 8) == 2
    assert hamming_Distance(2, 4) == 2
    assert hamming_Distance(1, 2) == 2