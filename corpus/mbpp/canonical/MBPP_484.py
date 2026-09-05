def remove_matching_tuple(test_list1, test_list2):
  res = [sub for sub in test_list1 if sub not in test_list2]
  return (res) 