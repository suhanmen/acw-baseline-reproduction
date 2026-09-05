def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(element % k == 0 for element in t):
            result.append(t)
    return result