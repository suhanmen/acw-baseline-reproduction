import re
def check_literals(text, patterns):
  for pattern in patterns:
    if re.search(pattern,  text):
        return ('Matched!')
    else:
        return ('Not Matched!')