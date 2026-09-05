import re

def snake_to_camel(s):
    if not s:
        return ''
    s = re.sub(r'(?<=_)([a-z]+)', lambda m: m.group().upper(), s)
    return s