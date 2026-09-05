import re

def remove_uppercase(s):
    return re.sub('[A-Z]', '', s)