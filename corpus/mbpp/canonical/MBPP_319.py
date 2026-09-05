import re
def find_long_word(text):
  return (re.findall(r"\b\w{5}\b", text))