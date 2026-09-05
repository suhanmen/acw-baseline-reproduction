def count_hexadecimal(lower: int, upper: int) -> int:
    """
    Count hexadecimal numbers in the given range [lower, upper].
    A number is considered 'hexadecimal' if its string representation 
    contains at least one digit from 'A' to 'F' (case-insensitive) 
    when converted to lowercase.

    Parameters:
    lower (int): Start of range (inclusive)
    upper (int): End of range (inclusive)

    Returns:
    int: Count of numbers in the range that contain hexadecimal digits A-F
    """
    count = 0
    for num in range(lower, upper + 1):
        hex_str = format(num, 'x')
        if any(c in 'abcdef' for c in hex_str):
            count += 1
    return count

# Verification
assert count_hexadecimal(10, 15) == 6, f"Test 1 failed: {count_hexadecimal(10, 15)}"
assert count_hexadecimal(2, 4) == 0, f"Test 2 failed: {count_hexadecimal(2, 4)}"
assert count_hexadecimal(15, 16) == 1, f"Test 3 failed: {count_hexadecimal(15, 16)}"