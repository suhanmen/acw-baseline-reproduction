def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    """
    # Check if the string is empty
    if not s:
        return False

    # Check if the string length is less than 3
    if len(s) < 3:
        return False

    # Iterate through each set of 3 consecutive characters
    for i in range(len(s) - 2):
        # Extract the triplet
        triplet = s[i:i+3]
        # Check if all three characters are distinct
        if len(set(triplet)) != 3:
            return False

    # All triplets are valid; the string is happy
    return True