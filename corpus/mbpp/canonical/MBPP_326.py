from collections import defaultdict 

def most_occurrences(test_list):
  temp = defaultdict(int)
  for sub in test_list:
    for wrd in sub.split():
      temp[wrd] += 1
  res = max(temp, key=temp.get)
  return (str(res)) 