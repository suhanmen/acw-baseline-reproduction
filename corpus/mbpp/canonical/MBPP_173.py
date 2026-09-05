import re
def remove_splchar(text): 
 pattern = re.compile('[\W_]+')
 return (pattern.sub('', text))