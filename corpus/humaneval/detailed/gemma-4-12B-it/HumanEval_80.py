from typing import Any

def is_happy(s: Any) -> bool:
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # Validate input type: The problem implies s is a string.
    # If input is not a string, we treat it as non-happy or handle as an error.
    if not isinstance(s, str):
        return False

    # Requirement 1: Length must be at least 3.
    string_length = len(s)
    if string_length < 3:
        return False

    # Requirement 2: Every 3 consecutive letters must be distinct.
    # We iterate through the string, checking every window of size 3.
    # The loop will stop at string_length - 2 to ensure index + 2 is within bounds.
    for i in range(string_length - 2):
        # Extract the current window of 3 characters
        char_1 = s[i]
        char_2 = s[i + 1]
        char_3 = s[i + 2]

        # Check for distinctness within the triplet.
        # A triplet is distinct if no two characters are the same.
        # We check all three pairs within the window.
        is_pair_1_2_distinct = (char_1 != char_2)
        is_pair_2_3_distinct = (char_2 != char_3)
        is_pair_1_3_distinct = (char_1 != char_3)

        # If any pair within the window of 3 is equal, the string is not happy.
        if not (is_pair_1_2_distinct and is_pair_2_3_distinct and is_pair_1_3_distinct):
            return False

    # If we have passed all length and distinctness checks, the string is happy.
    return True