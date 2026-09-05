def first_non_repeating_character(s):
    if not s:
        return None

    frequency = {}

    # Count the frequency of each character
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Iterate through the string to find the first non-repeated character
    for char in s:
        if frequency[char] == 1:
            return char

    # If all characters are repeated
    return None

# Test cases
print(first_non_repeating_character("abcabc"))  # Output: None
print(first_non_repeating_character("abc"))     # Output: "a"
print(first_non_repeating_character("ababc"))   # Output: "c")