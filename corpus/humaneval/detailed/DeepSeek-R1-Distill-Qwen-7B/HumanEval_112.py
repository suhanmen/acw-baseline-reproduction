def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Check if inputs are valid
    if not isinstance(s, str) or not isinstance(c, str):
        return (None, False)

    if not c:
        # If c is empty, return original s and check palindrome
        result = s
        is_palindrome = result == result[::-1]
        return (result, is_palindrome)

    # Convert s to list for easier manipulation
    s_list = list(s)

    # Remove characters from s that are in c
    for char in s_list:
        if char in c:
            s_list.remove(char)

    result = ''.join(s_list)

    # Check if the result is palindrome
    is_palindrome = result == result[::-1]

    return (result, is_palindrome)