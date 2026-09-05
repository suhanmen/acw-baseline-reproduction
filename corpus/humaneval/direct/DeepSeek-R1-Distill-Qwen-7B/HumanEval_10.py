def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ""
    max_len = len(string)
    # Find the longest palindromic suffix
    for i in range(max_len, 0, -1):
        # substring from 0 to i
        substr = string[:i]
        if is_palindrome(substr):
            # the part to reverse is from 0 to i-1, excluding the palindromic part
            prefix = string[:i-1]
            return prefix[::-1] + string
    return string[::-1] + string  # fallback case when no palindrome found