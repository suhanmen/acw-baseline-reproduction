def count_odd(array_nums):
   count_odd = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
   return count_odd