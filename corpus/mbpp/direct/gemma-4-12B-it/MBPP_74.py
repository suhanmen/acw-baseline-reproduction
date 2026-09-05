def is_samepatterns(pattern1: list, pattern2: list) -> bool:
    """
    Checks if the two lists follow the same pattern of mapping.
    Each unique element in pattern1 must map to exactly one unique element in pattern2,
    and vice versa. The lengths of both lists must also be equal.
    """
    if len(pattern1) != len(pattern2):
        return False

    mapping1 = {}
    mapping2 = {}

    for p1, p2 in zip(pattern1, pattern2):
        # Check if p1 is already mapped to something other than p2
        if p1 in mapping1 and mapping1[p1] != p2:
            return False
        # Check if p2 is already mapped to something other than p1
        if p2 in mapping2 and mapping2[p2] != p1:
            return False

        mapping1[p1] = p2
        mapping2[p2] = p1

    return True