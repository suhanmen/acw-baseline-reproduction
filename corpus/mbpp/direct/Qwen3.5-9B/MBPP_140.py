def extract_singly(tuples_list):
    from collections import defaultdict

    count_map = defaultdict(int)

    for t in tuples_list:
        for element in t:
            count_map[element] += 1

    result = []
    seen = set()

    # Iterate in insertion order of first appearance
    for t in tuples_list:
        for element in t:
            if count_map[element] == 1 and element not in seen:
                result.append(element)
                seen.add(element)

    return result