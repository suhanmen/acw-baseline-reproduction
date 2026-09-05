def check(s: str) -> str:
    """
    Checks whether the given string is a binary string (contains only '0' and '1').

    Args:
        s (str): The string to check.

    Returns:
        str: "Yes" if the string is binary, "No" otherwise.
    """
    if not s:
        return "No"

    for char in s:
        if char not in ('0', '1'):
            return "No"
    return "Yes"