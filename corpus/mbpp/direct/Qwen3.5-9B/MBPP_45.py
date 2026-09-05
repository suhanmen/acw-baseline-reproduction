from math import gcd
from functools import reduce

def get_gcd(arr):
    return reduce(gcd, arr)