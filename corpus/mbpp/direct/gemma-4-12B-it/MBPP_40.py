from collections import Counter

def freq_element(list_of_lists):
    """
    Finds the frequency of elements in a given list of lists using the collections module.
    """
    # Flatten the list of lists and count occurrences
    counts = Counter()
    for sublist in list_of_lists:
        counts.update(sublist)
    return dict(counts)