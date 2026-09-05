def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    if not text:
        return True
    lower_text = text.lower()
    for i in range(len(lower_text) // 2):
        if lower_text[i] != lower_text[-(i + 1)]:
            return False
    return True