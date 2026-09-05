from itertools import groupby
def encode_list(list1):
    return [[len(list(group)), key] for key, group in groupby(list1)]