def remove_tuples(test_list, K):
  res = [ele for ele in test_list if len(ele) != K]
  return (res) 