def hamming_distance(a, b):
    """
    Calculate the Hamming distance between two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The Hamming distance, which is the number of positions with different bits.
    """
    # Handle the case where either a or b is not an integer
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")

    # Calculate the XOR of the two numbers
    xor_result = a ^ b

    # Count the number of set bits in the XOR result
    distance = bin(xor_result).count('1')

    return distance

# Test cases to validate the function
assert hamming_distance(4, 8) == 2, "Test case 4 and 8 failed"
assert hamming_distance(2, 4) == 2, "Test case 2 and 4 failed"
assert hamming_distance(1, 2) == 2, "Test case 1 and 2 failed"

print("All test cases passed successfully.")