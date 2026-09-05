def replace_max_specialchar(text: str, n: int) -> str:
    """
    Replace maximum n occurrences of spaces, commas, or dots with a colon.
    """
    if n <= 0:
        return text

    special_chars = {' ', ',', '.'}
    result = []
    count = 0

    for char in text:
        if char in special_chars and count < n:
            result.append(':')
            count += 1
        else:
            result.append(char)

    return ''.join(result)