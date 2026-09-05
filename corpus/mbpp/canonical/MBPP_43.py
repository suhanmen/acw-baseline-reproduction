import re
def text_match(text):
  patterns = '^[a-z]+_[a-z]+$'
  if re.search(patterns,  text):
    return ('Found a match!')
  else:
    return ('Not matched!')