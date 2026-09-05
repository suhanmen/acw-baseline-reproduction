from collections import Counter

def freq_element(lst):
    flattened = [num for sublist in lst for num in sublist]
    return dict(Counter(flattened))