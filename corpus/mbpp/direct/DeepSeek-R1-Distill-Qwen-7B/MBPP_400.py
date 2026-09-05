def extract_freq(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return max(freq.values())