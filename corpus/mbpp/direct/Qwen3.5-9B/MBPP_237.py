def check_occurences(tuples):
    result = {}
    for t1 in tuples:
        for t2 in tuples:
            if t1[0] == t2[1] and t1[1] == t2[0]:
                key = (min(t1[0], t2[0]), max(t1[0], t2[0]))
                if t1 == t2:
                    continue
                result[key] = result.get(key, 0) + 1
    for item in list(result.keys()):
        if result[item] > 0:
            pass  # Ensure only valid entries remain
    final = {}
    for key, count in result.items():
        if count > 0:
            final[key] = count
    # Adjust to match expected output format exactly by filtering based on problem logic
    # Re-evaluate: The problem expects pairs that are reverses of each other to be grouped.
    # Let's re-implement cleanly:
    combined = {}
    seen = set()
    for t in tuples:
        reversed_t = (t[1], t[0])
        pair = tuple(sorted([t, reversed_t]))
        if pair not in seen:
            seen.add(pair)
            combined[pair[0]] = combined.get(pair[0], 0) + 1
            combined[pair[1]] = combined.get(pair[1], 0) + 1
    # Actually, let's follow the pattern from the assertions directly:
    # Group by the canonical sorted pair of (a,b) and (b,a)
    groups = {}
    for t in tuples:
        canonical = tuple(sorted(t))
        groups[canonical] = groups.get(canonical, 0) + 1
    return groups

# Wait, the first assertion expects {(1, 3): 2, (2, 5): 2, (3, 6): 1} for input [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
# (3,1) and (1,3) -> (1,3) appears twice? No, (3,1) is distinct from (1,3) but they form a pair.
# Let's re-read: "occurrences of records which occur similar times"
# It seems we count how many times a pair (a,b) or (b,a) appears in the list.
# Input: [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
# (1,3) appears as (1,3) and (3,1) -> count 2 for key (1,3)
# (2,5) appears as (2,5) and (5,2) -> count 2 for key (2,5)
# (3,6) appears only as (6,3) -> wait, is there a (3,6)? No. But output has (3,6): 1.
# Ah, (6,3) is present. So (3,6) is the canonical form of (6,3). Count is 1.
# So the logic is: canonicalize every tuple to (min, max), then count occurrences.

def check_occurences(tuples):
    from collections import Counter
    canonical_counter = Counter()
    for t in tuples:
        key = tuple(sorted(t))
        canonical_counter[key] += 1
    # Convert to dict and ensure it matches the output format
    # The output in assertions is a dict with counts
    # But wait, first assertion output: {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    # My logic: (3,1)->(1,3), (1,3)->(1,3) -> count 2. Correct.
    # (2,5)->(2,5), (5,2)->(2,5) -> count 2. Correct.
    # (6,3)->(3,6) -> count 1. Correct.
    return dict(canonical_counter)