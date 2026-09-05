def check_occurences(tuples_list):
    """
    Identifies records that occur similar times in the given tuples.
    A 'similar' occurrence is interpreted as the same set of numbers 
    (unordered) appearing in the list. However, looking at the assertions:
    - (3, 1) and (1, 3) are treated as the same record (3, 1).
    - (2, 5) and (5, 2) are treated as (2, 5).
    - (6, 3) and (3, 6) are treated as (3, 6).
    - (4, 2) and (2, 4) are treated as (2, 4).
    - (6, 3) and (3, 6) are treated as (3, 6).
    - (25, 12) and (12, 25) are treated as (12, 25).

    The logic seems to be: 
    1. For each tuple, sort it to create a canonical key (e.g., (1, 3)).
    2. Count occurrences of these canonical keys.
    3. The result dictionary contains the sorted tuple keys and their counts.
    4. Wait, looking at the first assertion: [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] 
       -> {(1, 3): 2, (2, 5): 2, (3, 6): 1}
       Here (6, 3) becomes (3, 6).
    5. Looking at the second assertion: [(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)]
       -> {(2, 4): 2, (3, 6): 2, (4, 7): 1}
       Wait, (7, 4) becomes (4, 7).
    6. Looking at the third assertion: [(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)]
       -> {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}

    Correct Logic:
    - For each tuple in the list, sort it to get a canonical tuple (e.g., (min, max)).
    - Count the occurrences of these canonical tuples.
    - Return a dictionary of {canonical_tuple: count}.
    """
    counts = {}
    for t in tuples_list:
        # Create a canonical form: a tuple sorted in ascending order
        canonical = tuple(sorted(t))
        counts[canonical] = counts.get(canonical, 0) + 1
    return counts