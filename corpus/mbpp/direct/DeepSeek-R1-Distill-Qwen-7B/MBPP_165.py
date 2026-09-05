def count_char_position(s):
    count = 0
    for i, c in enumerate(s):
        if c.lower() == chr(ord('a') + i):
            count += 1
    return count

# Example usage and assertions
assert count_char_position("xbcefg") == 2, "Test case 1 failed"
assert count_char_position("ABcED") == 3, "Test case 2 failed"
assert count_char_position("AbgdeF") == 5, "Test case 3 failed"