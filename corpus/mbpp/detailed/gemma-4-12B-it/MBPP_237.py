from typing import List, Tuple, Dict

def check_occurences(data: List[Tuple[int, int]]) -> Dict[Tuple[int, int], int]:
    """
    Analyzes a list of tuples to find the frequency of occurrences of pairs
    sorted by their internal values.

    The logic follows these steps:
    1. Validate the input.
    2. For each tuple (a, b), identify a "canonical" form where the smaller 
       value comes first. This ensures (1, 3) and (3, 1) are treated as the same pair.
    3. Count the occurrences of these canonical forms.
    4. The final output includes the canonical form as the key and its count as the value.

    Note: Based on the provided assertions, if a pair (a, b) exists in the input, 
    the output key is the sorted version (min(a, b), max(a, b)).
    """
    # 1. Input Validation
    if not isinstance(data, list):
        raise ValueError("Input must be a list of tuples.")

    if not data:
        return {}

    # Dictionary to store the frequency of canonical pairs
    # Key: Tuple[int, int] (sorted), Value: int (count)
    counts: Dict[Tuple[int, int], int] = {}

    # 2. Process every record in the input
    for record in data:
        # Validate that each element is a tuple of exactly 2 integers
        if not isinstance(record, tuple) or len(record) != 2:
            raise ValueError(f"Invalid record format: {record}. Expected a tuple of 2 integers.")

        val1 = record[0]
        val2 = record[1]

        if not isinstance(val1, int) or not isinstance(val2, int):
            raise ValueError(f"Record values must be integers. Found: {val1}, {val2}")

        # 3. Create a canonical representation
        # Sorting the pair ensures (3, 1) and (1, 3) are mapped to (1, 3)
        if val1 < val2:
            canonical_pair = (val1, val2)
        elif val1 > val2:
            canonical_pair = (val2, val1)
        else:
            # Case where the two numbers are equal (e.g., (3, 3))
            canonical_pair = (val1, val2)

        # 4. Update the frequency map
        if canonical_pair in counts:
            counts[canonical_pair] += 1
        else:
            counts[canonical_pair] = 1

    # The assertions provided in the prompt have a specific nuance:
    # Let's re-examine the first assertion:
    # input: [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
    # canonical pairs: (1, 3), (1, 3), (2, 5), (2, 5), (3, 6)
    # expected: {(1, 3): 2, (2, 5): 2, (3, 6): 1}

    # The logic holds.
    return counts

# The following code block contains the implementation described above.
# It handles empty lists, non-integer types, and unsorted pairs.