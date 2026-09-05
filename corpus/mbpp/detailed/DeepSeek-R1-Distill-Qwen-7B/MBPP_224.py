def count_Set_Bits(number):
    # Input Validation
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer.")

    # Count Set Bits using binary string method
    binary_string = bin(number)[2:]  # Convert to binary and remove '0b' prefix
    set_bits = binary_string.count('1')

    return set_bits

# Test Cases
assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2