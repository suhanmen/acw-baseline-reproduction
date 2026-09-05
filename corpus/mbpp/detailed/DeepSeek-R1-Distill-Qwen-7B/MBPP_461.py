def upper_ctr(s):
    # Input validation: check if s is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    # Initialize the counter for uppercase characters
    upper_counter = 0

    # Iterate through each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Increment the counter if it is
            upper_counter += 1

    # Return the total count of uppercase characters
    return upper_counter

# Test cases to verify the correctness of the function
assert upper_ctr('PYthon') == 1, "Test case 1 failed"
assert upper_ctr('BigData') == 1, "Test case 2 failed"
assert upper_ctr('program') == 0, "Test case 3 failed"