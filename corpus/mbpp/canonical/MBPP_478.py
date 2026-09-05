import re
def remove_lowercase(str1):
 remove_lower = lambda text: re.sub('[a-z]', '', text)
 result =  remove_lower(str1)
 return result