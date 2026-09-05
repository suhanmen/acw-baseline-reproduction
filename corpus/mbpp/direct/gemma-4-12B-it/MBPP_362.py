from collections import Counter

def max_occurrences(lst):
    if not lst:
        return None

    counts = Counter(lst)
    max_count = max(counts.values())

    modes = [item for item, count in counts.items() if count == max_count]

    # Sort modes to ensure deterministic order if needed, 
    # though the requirement implies specific output formats.
    # The assert requires 1,0 which is a tuple or list depending on interpretation.
    # Given the structure of the assertions, we handle single vs multiple results.

    if len(modes) == 1:
        return modes[0]
    else:
        # The assertion [1,2,6,7,0,1,0,1,0] == 1,0 suggests returning a tuple
        # of the items that appear most frequently.
        return tuple(sorted(modes, key=lambda x: (counts[x], x))) if len(modes) > 1 else modes[0]

# Re-evaluating the specific assertion: max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
# In Python, 1,0 is a tuple (1, 0). 
# Let's refine the logic to match the exact requested output types.

def max_occurrences(lst):
    if not lst:
        return None

    counts = Counter(lst)
    max_val = max(counts.values())

    # Find all keys that have the max_val
    # The order in the tuple (1,0) suggests sorting by value or first appearance.
    # Since 1 and 0 both appear 3 times, we need to match (1, 0).
    modes = [item for item, count in counts.items() if count == max_val]

    if len(modes) == 1:
        return modes[0]
    else:
        # To match (1, 0) specifically from the input [1,2,6,7,0,1,0,1,0]
        # Order of appearance: 1 appears first, then 0.
        # Let's check if it needs to be sorted descending or by appearance.
        # 1,0 is a tuple. 1 comes before 0 in the input.
        res = []
        seen = set()
        for x in lst:
            if x in modes and x not in seen:
                res.append(x)
                seen.add(x)
        return tuple(res)

# Final check on the assertions:
# 1. [1,2,3,1,2,3,12,4,2] -> 1:3, 2:3, 3:2, 12:1, 4:1. Max is 3? 
# Wait, the assertion says max_occurrences([1,2,3,1,2,3,12,4,2]) == 2.
# Let's re-count: 1 appears 2 times, 2 appears 3 times, 3 appears 2 times.
# If it returns 2, it means it returns the ITEM that appears most.
# Correction: [1,2,3,1,2,3,12,4,2]
# 1: 2 times
# 2: 3 times
# 3: 2 times
# 12: 1 time
# 4: 1 time
# Max count is 3, which belongs to item '2'.

# 2. [1,2,6,7,0,1,0,1,0]
# 1: 3 times
# 2: 1 time
# 6: 1 time
# 7: 1 time
# 0: 3 times
# Max count is 3. Items are 1 and 0. Assertion wants 1,0 (tuple).

# 3. [1,2,3,1,2,4,1]
# 1: 3 times
# 2: 2 times
# 3: 1 time
# 4: 1 time
# Max count is 3. Item is 1.

def max_occurrences(lst):
    if not lst:
        return None
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1

    max_freq = max(counts.values())
    modes = []
    # To maintain order of appearance for the tuple
    seen = set()
    for x in lst:
        if counts[x] == max_freq and x not in seen:
            modes.append(x)
            seen.add(x)

    if len(modes) == 1:
        return modes[0]
    return tuple(modes)