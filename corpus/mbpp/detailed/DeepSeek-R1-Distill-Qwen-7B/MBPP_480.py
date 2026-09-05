def get_max_occuring_char(s):
    # Handle the case where the input string is empty
    if not s:
        return None  # or raise an appropriate exception if needed

    # Step 1: Count the frequency of each character
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Step 2: Find the maximum frequency
    max_freq = max(char_counts.values(), default=0)

    # Step 3: Find all characters with the maximum frequency
    max_chars = [char for char, count in char_counts.items() if count == max_freq]

    # Step 4: Return the alphabetically smallest character
    return min(max_chars)