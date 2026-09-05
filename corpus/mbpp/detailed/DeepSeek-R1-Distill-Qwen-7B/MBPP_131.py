def reverse_vowels(s):
    # Check if input is a string
    if not isinstance(s, str):
        return "invalid input"

    # Handle empty string
    if len(s) == 0:
        return ""

    # Convert string to list for manipulation
    char_list = list(s)

    # List to hold indices of vowels
    vowel_indices = []
    # List to hold vowels for reversal
    vowels = []

    # Iterate over each character to find vowels
    for i, char in enumerate(char_list):
        if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            vowel_indices.append(i)
            vowels.append(char)

    # Reverse the list of vowels
    reversed_vowels = vowels[::-1]

    # Replace the vowels in their original positions
    for idx, rev_char in zip(vowel_indices, reversed_vowels):
        char_list[idx] = rev_char

    # Join the list back into a string
    return ''.join(char_list)