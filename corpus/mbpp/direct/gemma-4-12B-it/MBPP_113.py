def check_integer(s: str) -> bool:
    """
    Checks if a given string represents an integer.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid integer, False otherwise.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    assert check_integer("python") == False
    assert check_integer("1") == True
    assert check_integer("12345") == True