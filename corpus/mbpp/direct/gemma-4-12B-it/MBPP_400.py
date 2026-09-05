def extract_freq(tuples_list):
    """
    Extracts the frequency of unique tuples in the given list regardless of order.
    Two tuples are considered the same if they contain the same elements.
    """
    unique_counts = {}
    for t in tuples_list:
        # Sort the tuple to make order irrelevant
        canonical_form = tuple(sorted(t))
        unique_counts[canonical_form] = unique_counts.get(canonical_form, 0) + 1

    # The problem asks for the count of unique tuples (items that appear in the list).
    # Based on the assertions:
    # [(3, 4), (1, 2), (4, 3), (5, 6)] -> (3,4) and (4,3) are the same. 
    # Unique tuples are: {(3,4), (1,2), (5,6)}. Count is 3.
    # [(4, 15), (2, 3), (5, 4), (6, 7)] -> All unique. Count is 4.
    # [(5, 16), (2, 3), (6, 5), (6, 9)] -> All unique. Count is 4.

    return len(unique_counts)

if __name__ == "__main__":
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)]) == 4
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)]) == 4