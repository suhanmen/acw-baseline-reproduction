def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its Roman numeral equivalent as a string,
    and return it in lowercase.

    Parameters:
    number (int): The integer to convert to a Roman numeral. Must be between 1 and 1000.

    Returns:
    str: The Roman numeral representation in lowercase.

    Raises:
    ValueError: If the input is not an integer, is less than 1, or greater than 1000.

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Validate input
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("number must be an integer between 1 and 1000 inclusive.")

    # Mapping of integer values to Roman numerals
    roman_numerals = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i'),
    ]

    roman_num = ''
    for value, numeral in roman_numerals:
        while number >= value:
            roman_num += numeral
            number -= value

    return roman_num