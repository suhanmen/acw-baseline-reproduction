def float_sort(price):
  float_sort=sorted(price, key=lambda x: float(x[1]), reverse=True)
  return float_sort