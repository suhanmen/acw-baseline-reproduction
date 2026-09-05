def check_k_elements(test_list, K):
  res = True
  for tup in test_list:
    for ele in tup:
      if ele != K:
        res = False
  return (res) 