def min_flip_to_make_string_alternate(binary_string):
    # Calculate flips needed for both possible patterns: starting with '0' and starting with '1'
    flips_starting_with_zero = 0
    flips_starting_with_one = 0

    for i, char in enumerate(binary_string):
        # Expected character for the two patterns at position i
        expected_char_0 = '0' if i % 2 == 0 else '1'
        expected_char_1 = '1' if i % 2 == 0 else '0'

        if char != expected_char_0:
            flips_starting_with_zero += 1
        if char != expected_char_1:
            flips_starting_with_one += 1

    # The minimum flips required is the lesser of the two
    return min(flips_starting_with_zero, flips_starting_with_one)

# Test the function with provided assertions
assert min_flip_to_make_string_alternate("0001010111") == 2, "First test case failed"
assert min_flip_to_make_string_alternate("001") == 1, "Second test case failed"
assert min_flip_to_make_string_alternate("010111011") == 2, "Third test case failed"