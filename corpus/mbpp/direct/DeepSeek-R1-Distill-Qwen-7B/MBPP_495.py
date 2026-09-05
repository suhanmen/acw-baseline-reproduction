import re

def remove_lowercase(s):
    return re.sub(r'[a-z]', '', s)