import re
def multiple_split(text):
  return (re.split('; |, |\*|\n',text))