def add_K_element(test_list, K):
  res = [tuple(j + K for j in sub ) for sub in test_list]
  return (res) 