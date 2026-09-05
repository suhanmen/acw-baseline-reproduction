def find_tuples(tuples_list, k):
    return [tup for tup in tuples_list if all(x % k == 0 for x in tup)]