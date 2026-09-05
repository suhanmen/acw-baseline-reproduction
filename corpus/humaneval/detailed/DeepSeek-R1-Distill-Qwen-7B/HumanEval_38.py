def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    if not s:
        return ""
    # Split string into groups of three characters each
    groups = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        groups.append(group)

    # Cycle each group if it has exactly three characters
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            groups[i] = groups[i][1] + groups[i][2] + groups[i][0]

    # Concatenate all groups to form the encoded string
    return ''.join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic and returns the decoded string.
    """
    if not s:
        return ""

    # Split the encoded string into groups of three characters each
    groups = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        groups.append(group)

    # Reverse cycle each group if it has exactly three characters
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            groups[i] = groups[i][2] + groups[i][0] + groups[i][1]

    # Concatenate all groups to form the decoded string
    return ''.join(groups)