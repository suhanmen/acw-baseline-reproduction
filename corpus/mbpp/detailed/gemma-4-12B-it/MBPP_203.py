from typing import Any

def hamming_Distance(n1: int, n2: int) -> int:
    """
    Calculates the Hamming distance between two integers.
    The Hamming distance is the number of positions at which the 
    corresponding bits are different.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int: The count of differing bits.

    Raises:
        TypeError: If inputs are not of type int.
        ValueError: If inputs are negative, as Hamming distance is 
                    typically defined for non-negative integers in bitwise contexts.
    """
    # Input Validation: Check types
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError(
            f"Inputs must be integers. Received types: {type(n1).__name__} and {type(n2).__name__}"
        )

    # Input Validation: Check for negative numbers
    # While bitwise operations work on negatives (two's complement), 
    # Hamming distance is standardly defined for positive bit representations.
    if n1 < 0 or n2 < 0:
        raise ValueError("Inputs must be non-negative integers.")

    # Edge Case: If both are zero, the distance is zero.
    if n1 == 0 and n2 == 0:
        return 0

    # Step 1: Use XOR to find differing bits.
    # The XOR operation (^) results in a binary number where bits are set 
    # to 1 only if the bits in n1 and n2 are different.
    xor_result: int = n1 ^ n2

    # Step 2: Count the number of set bits (1s) in the result.
    # We iterate through the bits of the xor_result.
    distance_count: int = 0
    temp_xor_result: int = xor_result

    # Standard bit counting algorithm (Brian Kernighan's algorithm)
    # This is more efficient than checking every bit position as it only 
    # iterates as many times as there are set bits.
    while temp_xor_result > 0:
        # This operation clears the least significant set bit.
        temp_xor_result = temp_xor_result & (temp_xor_result - 1)
        distance_count += 1

    return distance_count

if __name__ == "__main__":
    # Validation of provided assertions
    assert hamming_Distance(4, 8) == 2   # 4 is 0100, 8 is 1000 -> diffs at 2^2 and 2^3
    assert hamming_Distance(2, 4) == 2   # 2 is 0010, 4 is 0100 -> diffs at 2^1 and 2^2
    assert hamming_Distance(1, 2) == 2   # 1 is 0001, 2 is 0010 -> diffs at 2^0 and 2^1