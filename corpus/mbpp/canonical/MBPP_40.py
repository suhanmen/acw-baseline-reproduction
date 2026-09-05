from collections import Counter
from itertools import chain
def freq_element(nums):
  result = Counter(chain.from_iterable(nums))
  return result