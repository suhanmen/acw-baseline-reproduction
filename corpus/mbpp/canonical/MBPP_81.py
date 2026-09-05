def zip_tuples(test_tup1, test_tup2):
  res = []
  for i, j in enumerate(test_tup1):
    res.append((j, test_tup2[i % len(test_tup2)])) 
  return (res) 