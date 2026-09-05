def trim_tuple(tuples, k):
    return [[element for element in tup if abs(element) > k] for tup in tuples]