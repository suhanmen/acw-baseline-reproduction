def count_char_position(s):
    # Step 1: Normalize the input to uppercase
    normalized = s.upper()

    # Step 2: Check for valid characters
    for c in normalized:
        if not c.isalpha():
            return 0

    # Step 3: Initialize the count
    count = 0

    # Step 4: Iterate over each character in the normalized string
    for i, c in enumerate(normalized):
        # Determine the position in the alphabet
        alphabet_position = ord(c) - ord('A') + 1

        # Determine the position in the string
        string_position = i + 1

        # Check if positions match
        if alphabet_position == string_position:
            count += 1

    # Step 5: Return the count
    return count