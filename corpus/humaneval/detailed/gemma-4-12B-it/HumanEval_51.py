import typing

def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
    # Validate that the input is indeed a string
    if not isinstance(text, str):
        raise TypeError(f"Expected input type 'str', but received '{type(text).__name__}'")

    # Handle the edge case of an empty string explicitly
    if len(text) == 0:
        return ""

    # Define the set of vowels to be removed.
    # Using a set provides O(1) lookup time for each character check.
    # We include both lowercase and uppercase versions as per the requirements 
    # (e.g., 'aaBAA' -> 'B' implies uppercase 'A' is also removed).
    vowels_to_remove: typing.Set[str] = {
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    }

    # We will build the result string character by character.
    # Using a list to collect characters is more efficient than string concatenation 
    # in Python because strings are immutable.
    result_chars: typing.List[str] = []

    # Iterate through every character in the input string
    for char in text:
        # Check if the current character is a vowel
        is_vowel: bool = char in vowels_to_remove

        # If the character is not a vowel, append it to our result list
        if not is_vowel:
            result_chars.append(char)

    # Join the list of non-vowel characters back into a single string
    final_result: str = "".join(result_chars)

    return final_result