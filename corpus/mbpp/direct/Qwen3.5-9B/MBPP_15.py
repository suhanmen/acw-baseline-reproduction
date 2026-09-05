import re

def split_lowerstring(s):
    return re.findall(r'[A-Z]+|[a-z]', s)