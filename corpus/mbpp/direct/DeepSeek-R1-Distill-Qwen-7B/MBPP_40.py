from collections import defaultdict

def freq_element(list_of_lists):
    frequency = defaultdict(int)
    for sublist in list_of_lists:
        for element in sublist:
            frequency[element] += 1
    return dict(frequency)