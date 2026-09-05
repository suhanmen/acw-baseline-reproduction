def binary_to_decimal(binary_str):
    # Validate the input
    if not isinstance(binary_str, str) or any(c not in '01' for c in binary_str):
        raise ValueError("Invalid binary input")

    # Handle empty string case
    if len(binary_str) == 0:
        raise ValueError("Empty string is not valid")

    # Handle single character case
    if len(binary_str) == 1:
        return int(binary_str)

    # Reverse the binary string for easier processing
    reversed_binary = binary_str[::-1]

    result = 0
    for c in reversed_binary:
        result = (result << 1) | int(c)

    return result

# Example test cases
print(binary_to_decimal("100"))    # Output: 4
print(binary_to_decimal("1011"))   # Output: 11
print(binary_to_decimal("1101101")) # Output: 109