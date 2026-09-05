def count_Substring_With_Equal_Ends(s: str) -> int:
    n = len(s)
    count = 0
    # Iterate over all possible starting positions
    for i in range(n):
        # Iterate over all possible ending positions from start onwards
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1
    return count