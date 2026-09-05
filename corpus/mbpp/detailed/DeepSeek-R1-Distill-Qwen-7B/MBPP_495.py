import re

def remove_lowercase(s):
    pattern = r'[a-z]'
    return re.sub(pattern, '', s)