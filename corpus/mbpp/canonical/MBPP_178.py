import re
def string_literals(patterns,text):
  for pattern in patterns:
     if re.search(pattern,  text):
       return ('Matched!')
     else:
       return ('Not Matched!')