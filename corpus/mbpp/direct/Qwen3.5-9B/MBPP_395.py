def first_non_repeating_character(s: str) -> str:
    """
    Returns the first non-repeating character in the given string,
    or None if all characters are repeated.
    """
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in s:
        if count[ch] == 1:
            return ch

    return None