from collections import Counter

def count_samepair(lst1, lst2, lst3):
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    c3 = Counter(lst3)
    common_pairs = c1 & c2 & c3
    return sum(common_pairs.values())