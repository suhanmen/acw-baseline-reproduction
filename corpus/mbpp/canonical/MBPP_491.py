import math
def sum_gp(a,n,r):
 total = (a * (1 - math.pow(r, n ))) / (1- r)
 return total