def check_if_last_char_is_a_letter(txt):
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
    if not txt:
        return False

    last_char = txt[-1]

    # Check if the last character is alphabetical
    if not last_char.isalpha():
        return False

    # The condition "is not a part of a word" implies it must be 
    # separated from previous characters by a space.
    # In "apple pi e", 'e' is preceded by a space, so it's not part 
    # of a multi-character word.
    # In "apple pie", 'e' is preceded by 'i', so it is part of a word.

    if len(txt) == 1:
        return True

    # If the character before the last character is a space, 
    # then the last character is a standalone letter (not part of a word).
    return txt[-2] == ' '