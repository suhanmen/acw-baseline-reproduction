def extract_symmetric(test_list):
  temp = set(test_list) & {(b, a) for a, b in test_list}
  res = {(a, b) for a, b in temp if a < b}
  return (res) 