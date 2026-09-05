def count_Substring_With_Equal_Ends(s):
    n = len(s)
    if n == 0:
        return 0

    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # For each character, if it appears k times, it forms k*(k+1)/2 substrings
    total_count = 0
    for count in char_count.values():
        total_count += count * (count + 1) // 2

    return total_count