from collections import Counter

def frequency(arr, target):
    count = Counter(arr)
    return count[target]