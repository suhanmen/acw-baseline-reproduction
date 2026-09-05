def count_unset_bits(number):
    """
    Count the number of unset bits (0s) in the binary representation of a given number.
    """
    # Handle the case where number is 0 explicitly
    if number == 0:
        return 1

    # Convert the number to its binary representation without the '0b' prefix
    binary_str = bin(number)[2:]

    # Count the number of '0's in the binary string
    zero_count = binary_str.count('0')

    return zero_count

# Test the function with the given examples
assert count_unset_bits(2) == 1, "Test case 1 failed"
assert count_unset_bits(4) == 2, "Test case 2 failed"
assert count_unset_bits(6) == 1, "Test case 3 failed"

# Additional test cases
print(count_unset_bits(0))   # Expected output: 1
print(count_unset_bits(1))   # Expected output: 0
print(count_unset_bits(3))   # Expected output: 0
print(count_unset_bits(5))   # Expected output: 0