import re

def text_match_two_three(s):
    match = re.search(r'\ba{1}bbb+?', s)
    return 'Found a match!' if match else 'Not matched!'