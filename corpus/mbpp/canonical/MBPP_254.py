import re
def words_ae(text):
 list = re.findall("[ae]\w+", text)
 return list