import collections
import re

def most_occurrences(strings_list):
    word_counts = collections.defaultdict(int)
    first_occurrence = {}

    for s in strings_list:
        words = re.findall(r'\w+', s)
        for w in words:
            lw = w.lower()
            word_counts[lw] += 1
            if lw not in first_occurrence:
                first_occurrence[lw] = w

    max_count = 0
    best_word = ""

    # Iterate through first_occurrence to maintain order of appearance for ties
    for lw in first_occurrence:
        if word_counts[lw] > max_count:
            max_count = word_counts[lw]
            best_word = first_occurrence[lw]

    return best_word