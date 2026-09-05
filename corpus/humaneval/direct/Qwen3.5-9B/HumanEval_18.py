def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    count = 0
    i = 0
    while i <= len(string) - len(substring):
        if string[i:i+len(substring)] == substring:
            count += 1
            i += 1  # Move only one character to allow overlapping
        else:
            i += 1
    return count