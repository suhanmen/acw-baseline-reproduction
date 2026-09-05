def count_Substrings(s: str, n: int) -> int:
    """
    Counts the number of substrings where the sum of digits equals the length of the substring.
    Note: The parameter 'n' is provided in the signature but is not used in the logic
    consistent with the assertions provided (where n seems to represent the length of s).
    """
    count = 0
    length = len(s)
    # Iterate through all possible start and end indices of substrings
    for i in range(length):
        current_sum = 0
        for j in range(i, length):
            current_sum += int(s[j])
            substring_length = j - i + 1
            if current_sum == substring_length:
                count += 1
    return count