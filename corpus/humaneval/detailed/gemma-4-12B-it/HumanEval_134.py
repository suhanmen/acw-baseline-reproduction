import typing

def check_if_last_char_is_a_letter(txt: str) -> bool:
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

    # Defensive check: Ensure the input is actually a string.
    if not isinstance(txt, str):
        raise TypeError(f"Input must be a string, not {type(txt).__name__}")

    # Edge Case: Empty string.
    # The problem requires checking the last character. An empty string has no last character.
    if len(txt) == 0:
        return False

    # Step 1: Identify the last character of the string.
    last_char: str = txt[-1]

    # Step 2: Check if the last character is an alphabetical letter.
    # .isalpha() returns True if all characters in the string are alphabetic.
    is_last_char_alpha: bool = last_char.isalpha()

    # If the last character isn't a letter (e.g., a space, number, or punctuation),
    # the condition for returning True is immediately failed.
    if not is_last_char_alpha:
        return False

    # Step 3: Determine if the last character is "part of a word".
    # According to the rules:
    # - "apple pie" -> 'e' is the last char. It is part of the word "pie".
    # - "apple pi e" -> 'e' is the last char. It is a standalone character (separated by spaces).
    # - "apple pi e " -> ' ' is the last char. This fails because ' ' is not a letter.

    # A character is NOT part of a word (i.e., it is a standalone letter) if:
    # 1. It is preceded by a space OR it is the very first character in the string.
    # 2. It is followed by nothing (it is the end of the string).
    # 3. It is preceded by a space (specifically, the character before it must be a space).

    # However, the example "apple pie" ➞ False implies that if there are letters 
    # immediately preceding the last letter without a space, it is "part of a word".

    # Let's evaluate the condition "is not a part of a word":
    # In "apple pi e", 'e' is preceded by a space.
    # In "apple pie", 'e' is preceded by 'i' (not a space).

    is_part_of_word: bool = False

    # Check if there is a character before the last character.
    if len(txt) > 1:
        char_before_last: str = txt[-2]

        # If the character immediately before the last character is NOT a space,
        # then the last character is attached to another character, making it 
        # part of a word.
        if char_before_last != " ":
            is_part_of_word = True
    else:
        # If the string is only one character long (e.g., "a"), 
        # it is not part of a larger group of characters.
        is_part_of_word = False

    # Final Logic:
    # The function returns True if:
    # - The last character is a letter.
    # - AND it is NOT part of a word (meaning it's preceded by a space or is the only char).
    if is_last_char_alpha and not is_part_of_word:
        return True
    else:
        return False