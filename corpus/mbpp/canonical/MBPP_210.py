import re
def is_allowed_specific_char(string):
    get_char = re.compile(r'[^a-zA-Z0-9.]')
    string = get_char.search(string)
    return not bool(string)