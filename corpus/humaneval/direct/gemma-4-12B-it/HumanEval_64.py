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
    vowels = "aeiou"
    count = 0
    s_upper = s.upper()

    for i in range(len(s_upper)):
        char = s_upper[i]
        if char in "AEIOU":
            count += 1
        elif char == "Y" and i == len(s_upper) - 1:
            count += 1

    return count