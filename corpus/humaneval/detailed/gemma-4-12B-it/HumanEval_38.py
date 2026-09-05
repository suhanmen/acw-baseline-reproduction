def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Input Validation: Ensure the input is a string.
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Handle the edge case of an empty string explicitly.
    if s == "":
        return ""

    # Step 1: Split the encoded string into groups of length 3.
    # The encoding logic specifies that the string was divided into groups of 3.
    # We must replicate this grouping logic exactly.
    groups = []
    current_index = 0
    string_length = len(s)

    # We calculate the number of groups using the same logic as encode_cyclic.
    # (len + 2) // 3 is a common way to perform ceiling division by 3.
    num_groups = (string_length + 2) // 3

    for i in range(num_groups):
        start_pos = 3 * i
        end_pos = min(3 * i + 3, string_length)

        # Extract the group substring.
        group_substring = s[start_pos:end_pos]
        groups.append(group_substring)

    decoded_parts = []

    # Step 2: Reverse the cyclic shift for each group.
    for group in groups:
        group_length = len(group)

        # The encoding logic:
        # If len(group) == 3, the group was transformed from ABC to BCA (left shift by 1).
        # If len(group) < 3, the group remained unchanged.

        if group_length == 3:
            # To reverse a left shift by 1 (BCA -> ABC):
            # The element at index 0 (B) moves to the end.
            # The element at index 1 (C) moves to index 0.
            # The element at index 2 (A) moves to index 1.
            # Effectively, we perform a right shift by 1.

            first_char = group[0]
            remaining_chars = group[1:]

            # The original order was (remaining_chars + first_char)
            # e.g., "BCA" -> "CA" + "B" -> "CAB" is wrong.
            # Let's re-evaluate: 
            # Original: 0, 1, 2  (ABC)
            # Encoded: 1, 2, 0  (BCA)
            # To get from 1, 2, 0 back to 0, 1, 2:
            # The char at index 2 of the encoded group is the original index 0.
            # The char at index 0 of the encoded group is the original index 1.
            # The char at index 1 of the encoded group is the original index 2.
            # So: original_group[0] = encoded_group[2]
            #       original_group[1] = encoded_group[0]
            #       original_group[2] = encoded_group[1]

            char_at_0_encoded = group[0]
            char_at_1_encoded = group[1]
            char_at_2_encoded = group[2]

            original_group = (
                char_at_2_encoded + 
                char_at_0_encoded + 
                char_at_1_encoded
            )
            decoded_parts.append(original_group)
        else:
            # If the length is not 3, the encoding function did not change the group.
            decoded_parts.append(group)

    # Step 3: Join the decoded groups back into a single string.
    result = "".join(decoded_parts)
    return result