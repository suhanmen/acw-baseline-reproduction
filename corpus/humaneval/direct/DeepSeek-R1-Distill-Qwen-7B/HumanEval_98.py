def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:  # Check if the index is even
            char = s[i]
            if char in {'A', 'E', 'I', 'O', 'U'}:
                count += 1
    return count