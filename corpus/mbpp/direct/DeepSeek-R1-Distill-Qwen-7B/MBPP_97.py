def frequency_lists(lst):
    frequency = {}
    for sublist in lst:
        for element in sublist:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return frequency