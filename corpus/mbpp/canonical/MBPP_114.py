from collections import Counter 
def assign_freq(test_list):
  res = [(*key, val) for key, val in Counter(test_list).items()]
  return (str(res)) 