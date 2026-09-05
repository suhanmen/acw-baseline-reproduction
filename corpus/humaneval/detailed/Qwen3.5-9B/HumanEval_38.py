def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # Input validation: ensure input is a string
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    # Handle empty string explicitly
    if len(s) == 0:
        return s

    # split string to groups. Each of length 3.
    # Calculate the number of groups needed to cover the entire string
    total_groups_count = (len(s) + 2) // 3

    # Create list of groups using explicit loop logic for clarity
    groups = []
    for i in range(total_groups_count):
        start_index = 3 * i
        # Calculate end index ensuring it does not exceed string length
        end_index = min((3 * i + 3), len(s))
        # Extract the slice
        group_content = s[start_index:end_index]
        groups.append(group_content)

    # cycle elements in each group. Unless group has fewer elements than 3.
    # We create a new list to avoid modifying the reference structure unpredictably
    processed_groups = []
    for group in groups:
        if len(group) == 3:
            # Cycle: move first char to end (e.g., "abc" -> "bca")
            rotated_content = group[1:] + group[0]
        else:
            # If group has fewer than 3 characters (1 or 2), leave as is
            rotated_content = group
        processed_groups.append(rotated_content)

    return "".join(processed_groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Logic Analysis:
    Original (Len 3): ABC -> Encoded: BCA
    To reverse: BCA -> ABC
    Shift observed: The first character moved to the end.
    Inverse operation: Move the LAST character to the FRONT.
    Pattern: "BCA" -> take last ('A') + rest ("BC") -> "ABC".
    Formula: group[ -1 ] + group[:-1]
    """

    # Input validation: ensure input is a string
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    # Handle empty string explicitly (should remain empty)
    if len(s) == 0:
        return s

    # Split encoded string to groups. Each of length 3 (reusing slice logic from encoder)
    total_groups_count = (len(s) + 2) // 3

    encoded_groups = []
    for i in range(total_groups_count):
        start_index = 3 * i
        end_index = min((3 * i + 3), len(s))
        group_content = s[start_index:end_index]
        encoded_groups.append(group_content)

    # Apply inverse rotation to each group
    decoded_groups = []
    for group in encoded_groups:
        if len(group) == 3:
            # Inverse cycle: move last char to front (e.g., "bca" -> "abc")
            # Logic: take the last character, then append the rest of the string
            first_char = group[-1]
            remaining_chars = group[:-1]
            restored_content = first_char + remaining_chars
        else:
            # If group has fewer than 3 characters, it was not rotated by encoder,
            # so it remains unchanged in the decoder.
            restored_content = group
        decoded_groups.append(restored_content)

    return "".join(decoded_groups)