import re
def find_character(string):
  uppercase_characters = re.findall(r"[A-Z]", string) 
  lowercase_characters = re.findall(r"[a-z]", string) 
  numerical_characters = re.findall(r"[0-9]", string) 
  special_characters = re.findall(r"[, .!?]", string) 
  return uppercase_characters, lowercase_characters, numerical_characters, special_characters