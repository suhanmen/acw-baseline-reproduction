from collections import Counter

def frequency_lists(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        flat_list.extend(sublist)
    return dict(Counter(flat_list))