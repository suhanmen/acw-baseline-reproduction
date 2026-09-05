FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert string to lowercase for case-insensitive comparison
    s_lower = s.lower()
    count = 0

    # Check each character
    for i, char in enumerate(s_lower):
        if char in 'aeiou':
            count += 1
        elif char == 'y' and i == len(s_lower) - 1:
            count += 1

    return count