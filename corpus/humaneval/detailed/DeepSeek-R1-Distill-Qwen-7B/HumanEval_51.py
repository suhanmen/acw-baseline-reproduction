def remove_vowels(text):
    """
    Remove vowels from the given string.

    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Define vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Initialize an empty string to build the result
    result = ''

    # Iterate through each character in the input string
    for char in text:
        # Check if the character is not a vowel
        if char not in vowels:
            # Append non-vowel characters to the result
            result += char

    # Return the constructed string with vowels removed
    return result