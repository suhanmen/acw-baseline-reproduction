def get_perrin(n):
  if (n == 0):
    return 3
  if (n == 1):
    return 0
  if (n == 2):
    return 2 
  return get_perrin(n - 2) + get_perrin(n - 3)