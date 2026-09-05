def count(input_string: str, char: str) -> int:
    """
    Counts the occurrence of a given character in a string.

    Args:
        input_string (str): The string to search within.
        char (str): The character to count.

    Returns:
        int: The number of times the character appears in the string.
    """
    return input_string.count(char)

if __name__ == "__main__":
    assert count("abcc", "c") == 2
    assert count("ababca", "a") == 3
    assert count("mnmm0pm", "m") == 4