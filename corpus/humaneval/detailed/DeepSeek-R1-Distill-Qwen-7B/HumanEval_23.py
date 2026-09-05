def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    if not isinstance(string, str):
        raise ValueError("Input must be a string")

    if string is None:
        raise ValueError("Input cannot be None")

    if len(string) == 0:
        return 0

    char_count = 0
    for char in string:
        char_count += 1

    return char_count