def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Check if input is a string
    if not isinstance(s, str):
        return 0

    # Convert to lowercase to handle case insensitivity
    s = s.lower()

    # Initialize vowel counter
    vowel_count = 0

    # Iterate over each character in the string
    for char in s:
        if char in {'a', 'e', 'i', 'o', 'u'}:
            vowel_count += 1

    # Special case for 'y' at the end of the string
    if s.endswith('y'):
        vowel_count += 1

    return vowel_count