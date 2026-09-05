def first_non_repeating_character(s):
    # Track the count of each character
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Check each character's count
    for char in s:
        if count[char] == 1:
            return char

    # If no non-repeating character found
    return None