import re
def replace_max_specialchar(text,n):
 return (re.sub("[ ,.]", ":", text, n))