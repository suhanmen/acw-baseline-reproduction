from collections import defaultdict

def max_aggregate(tuple_list):
    totals = defaultdict(int)
    for name, value in tuple_list:
        totals[name] += value
    return max(totals.items(), key=lambda item: item[1])