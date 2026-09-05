import re
def remove_uppercase(str1):
  remove_upper = lambda text: re.sub('[A-Z]', '', text)
  result =  remove_upper(str1)
  return (result)