def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # Split string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle each group if it has exactly three characters
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split encoded string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Un-cycle each group if it has exactly three characters
    groups = [(group[2] + group[0:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)