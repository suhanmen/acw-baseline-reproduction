def remove_replica(test_tup):
  temp = set()
  res = tuple(ele if ele not in temp and not temp.add(ele) 
				else 'MSP' for ele in test_tup)
  return (res)