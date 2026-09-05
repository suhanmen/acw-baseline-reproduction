def get_Odd_Occurrence(lst):
    if not lst:
        return None

    element_counts = {}
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    for element, count in element_counts.items():
        if count % 2 != 0:
            return element

    return None  # This line is theoretically unreachable