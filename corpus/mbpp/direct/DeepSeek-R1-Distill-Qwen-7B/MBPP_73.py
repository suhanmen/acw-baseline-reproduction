import re

def multiple_split(s):
    return re.split(
        r'(?<!\\)(?=\s*(\n|\\)|[\t\x0c\r])',  # Split on any whitespace or the given delimiters
        s
    )

# The code is complete and runnable on its own.