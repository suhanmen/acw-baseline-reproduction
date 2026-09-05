def string_literals(literals, text):
    """
    Checks if all strings in the literals list are present in the given text.

    Args:
        literals (list): A list of string literals to search for.
        text (str): The string to search within.

    Returns:
        str: 'Matched!' if all literals are found, 'Not Matched!' otherwise.
    """
    for literal in literals:
        if literal not in text:
            return 'Not Matched!'
    return 'Matched!'