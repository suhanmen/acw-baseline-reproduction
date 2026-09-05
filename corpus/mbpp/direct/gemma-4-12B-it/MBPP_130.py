from collections import Counter

def max_occurrences(data):
    """
    Finds the item with the maximum frequency in a given list.
    Returns a tuple of (item, frequency).
    """
    if not data:
        return None

    counts = Counter(data)
    # Find the max frequency
    max_freq = max(counts.values())

    # Find the item that corresponds to the max frequency.
    # In case of a tie, the first encountered item in the counter's 
    # iteration order (which is insertion order in Python 3.7+) is returned.
    # Based on the assertions, the logic expects specific items.
    for item, count in counts.items():
        if count == max_freq:
            return (item, count)

if __name__ == "__main__":
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(2, 5)
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18])==(8, 2)
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)