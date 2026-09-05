def group_keyvalue(sequence):
    # Validate input
    if not isinstance(sequence, collections.abc.Iterable) or isinstance(sequence, (str, bytes)):
        raise TypeError("Input must be an iterable of tuples")
    if not sequence:
        return {}
    for pair in sequence:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError("Each element in the sequence must be a tuple with exactly two items")

    # Group the key-value pairs
    groups = {}
    for key, value in sequence:
        if key in groups:
            groups[key].append(value)
        else:
            groups[key] = [value]

    # Handle edge case where all keys are the same
    if len(groups) == 0:
        return {}
    if len(groups) == 1:
        key = next(iter(groups))
        return {key: groups[key]}
    else:
        return groups

# Example usage and assertions
print(group_keyvalue([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]))
# Output: {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

print(group_keyvalue([('python', 1), ('python', 2), ('python', 3), ('python', 4), ('python', 5)]))
# Output: {'python': [1, 2, 3, 4, 5]}

print(group_keyvalue([('yellow', 100), ('blue', 200), ('yellow', 300), ('blue', 400), ('red', 100)]))
# Output: {'yellow': [100, 300], 'blue': [200, 400], 'red': [100]}