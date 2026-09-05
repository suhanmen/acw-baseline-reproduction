def group_tuples(tuples_list):
    from collections import defaultdict

    groups = defaultdict(list)
    for group in tuples_list:
        key = group[0]
        groups[key].append(group[1])

    result = []
    for key in groups:
        group_list = groups[key]
        if len(group_list) == 0:
            continue
        # The first element remains the same, and we concatenate all the following elements
        result.append([key] + [e for e in group_list[1:]])

    return result

# Test the function with provided assertions
assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]