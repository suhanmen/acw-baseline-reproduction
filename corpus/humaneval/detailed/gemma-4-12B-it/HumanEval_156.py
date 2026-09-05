import typing

def int_to_mini_roman(number: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Validate that the input is an integer
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, but received {type(number).__name__}.")

    # Validate the range restrictions (1 <= num <= 1000)
    if number < 1:
        raise ValueError(f"Input must be a positive integer (>= 1), but received {number}.")
    if number > 1000:
        raise ValueError(f"Input must not exceed 1000, but received {number}.")

    # Define the mapping of values to roman numeral symbols.
    # We use a list of tuples to maintain descending order of values.
    # Standard Roman Numerals for values up to 1000:
    # M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1
    roman_mapping: typing.List[typing.Tuple[int, str]] = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i")
    ]

    # This list will store the resulting components of the roman numeral string
    result_parts: typing.List[str] = []

    # Remaining value to process
    remaining_value: int = number

    # Iterate through the mapping to build the roman numeral
    for value, symbol in roman_mapping:
        # Determine how many times the current symbol fits into the remaining value
        # Using floor division to get the count
        count: int = remaining_value // value

        if count > 0:
            # Append the symbol to the parts list 'count' times
            # Using a loop to keep logic explicit as requested
            for _ in range(count):
                result_parts.append(symbol)

            # Subtract the total value accounted for by these symbols
            remaining_value -= (count * value)

        # Optimization: if the remaining value hits zero, we can stop early
        if remaining_value == 0:
            break

    # Join the list into a single string
    final_roman_string: str = "".join(result_parts)

    return final_roman_string