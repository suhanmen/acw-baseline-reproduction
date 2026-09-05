import re
def is_decimal(num):
  num_fetch = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
  result = num_fetch.search(num)
  return bool(result)