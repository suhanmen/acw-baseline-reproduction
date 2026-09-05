import re
from typing import Final

def remove_uppercase(input_string: str) -> str:
    """
    Removes all uppercase letters from a given string using regular expressions.

    Args:
        input_string (str): The source string containing mixed-case characters.

    Returns:
        str: The resulting string with all uppercase characters removed.

    Raises:
        TypeError: If the input_string is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, received {type(input_string).__name__}")

    # Handle empty string edge case
    if not input_string:
        return ""

    # Define the regex pattern for uppercase letters.
    # [A-Z] matches any single character in the range A to Z.
    # This assumes standard ASCII uppercase. 
    # If Unicode support is needed, re.UNICODE flag or \p{Lu} (via 'regex' module)
    # would be used, but for standard problems, [A-Z] is the standard.
    uppercase_pattern: Final[str] = r"[A-Z]"

    # Compile the regex pattern for better performance and clarity
    regex_compiled: re.Pattern = re.compile(uppercase_pattern)

    # Use re.sub to replace all occurrences of the pattern with an empty string.
    # result_string is the transformation of the input_string.
    result_string: str = regex_compiled.sub("", input_string)

    return result_string

# Defensive verification (matching the requested behavior)
if __name__ == "__main__":
    # Assertions provided in the prompt
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

    # Additional edge cases
    assert remove_uppercase('') == ''
    assert remove_uppercase('ABC') == ''
    assert remove_uppercase('abc') == 'abc'
    assert remove_uppercase('123!@#') == '123!@#'
    assert remove_uppercase('A') == ''
    assert remove_uppercase('a') == 'a'