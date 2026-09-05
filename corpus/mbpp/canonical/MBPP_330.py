import re
def find_char(text):
  return (re.findall(r"\b\w{3,5}\b", text))