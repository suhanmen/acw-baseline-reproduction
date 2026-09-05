from typing import List


def is_samepatterns(patterns1: List[str], patterns2: List[str]) -> bool:
    """
    Checks whether two lists of strings follow the same pattern.

    The rule is that there must be a one-to-one mapping between 
    the elements of the first list and the elements of the second list.

    Example:
    ["red", "green", "green"] and ["a", "b", "b"] is True 
    because:
    "red" -> "a"
    "green" -> "b"

    Example:
    ["red", "green", "greenn"] and ["a", "b", "b"] is False 
    because the length of the sequences is different.
    """

    # 1. Input Validation: Check if inputs are lists
    if not isinstance(patterns1, list) or not isinstance(patterns2, list):
        raise TypeError("Both inputs must be lists of strings.")

    # 2. Check if all elements are strings
    for item in patterns1:
        if not isinstance(item, str):
            raise TypeError("All elements in the first pattern must be strings.")
    for item in patterns2:
        if not isinstance(item, str):
            raise TypeError("All elements in the second pattern must be strings.")

    # 3. Length check: Patterns must have the same length to be compared
    len1 = len(patterns1)
    len2 = len(patterns2)

    if len1 != len2:
        return False

    # 4. Edge case: Empty lists
    if len1 == 0:
        return True

    # 5. Mapping Logic
    # We need to ensure a bijection (one-to-one and onto) between elements.
    # This means:
    # - Every unique string in list1 must map to exactly one unique string in list2.
    # - Every unique string in list2 must be mapped from exactly one unique string in list1.

    # Map to store pattern1_string -> pattern2_string
    map_p1_to_p2 = {}
    # Set to track which strings from pattern2 have already been assigned to a string in pattern1
    # This ensures the "one-to-one" property (no two different p1 strings map to the same p2)
    assigned_p2_values = set()

    for s1, s2 in zip(patterns1, patterns2):
        # If we have seen s1 before
        if s1 in map_p1_to_p2:
            # Check if it maps to the same s2 as before
            expected_s2 = map_p1_to_p2[s1]
            if expected_s2 != s2:
                return False
        else:
            # If s1 is new, we check if s2 has already been mapped to a different s1
            if s2 in assigned_p2_values:
                # This means s2 is already paired with a different string in patterns1
                return False

            # Establish the new mapping
            map_p1_to_p2[s1] = s2
            assigned_p2_values.add(s2)

    return True