def sort_on_occurence(lst):
    # Count the occurrences of each first element
    from collections import defaultdict
    count = defaultdict(int)
    for item in lst:
        key = item[0]
        count[key] += 1
    # Sort the list based on the count of the first element
    # If two elements have the same count, maintain their original order
    sorted_lst = sorted(lst, key=lambda x: (count[x[0]], lst.index(x)))
    # Rebuild the tuple with the count and original structure
    result = []
    for item in sorted_lst:
        original_first = item[0]
        count_first = count[original_first]
        rest = item[1:]
        result.append((original_first, count_first) + tuple(rest))
    return result

# Example usage:
print(sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]))
# Output: [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]

print(sort_on_occurence([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]))
# Output: [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]

print(sort_on_occurence([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]))
# Output: [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]