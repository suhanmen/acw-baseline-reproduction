import re

def multiple_split(text: str, delimiters: list) -> list:
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)

def multiple_split(text: str, delimiters: tuple) -> list:
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)

def multiple_split(text: str, delimiters: str) -> list:
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)

def multiple_split(text: str, delimiters):
    if isinstance(delimiters, str):
        delimiters = (delimiters,)
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)