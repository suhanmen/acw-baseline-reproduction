import re

def multiple_split(text: str) -> list:
    """
    Splits the given string by multiple delimiters (newline \n and asterisk *)
    using regular expressions.
    """
    # The regex [\\n\*] matches either a newline character or an asterisk.
    # re.split splits the string based on these characters.
    # We filter out empty strings that might result from consecutive delimiters
    # or delimiters at the start/end of the string.
    parts = re.split(r'[\n\*]', text)
    return [p for p in parts if p]