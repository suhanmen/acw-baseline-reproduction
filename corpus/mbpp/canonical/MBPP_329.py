def neg_count(list):
  neg_count= 0
  for num in list: 
    if num <= 0: 
      neg_count += 1
  return neg_count 