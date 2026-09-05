def sort_on_occurence(lst):
    if not lst:
        return []

    # Helper function to count occurrences of each identifier
    def count_identifiers(lst):
        counts = {}
        for item in lst:
            identifier = item[0]
            counts[identifier] = counts.get(identifier, 0) + 1
        return counts

    # Helper function to sort a list based on the count of each element
    def sort_by_count(lst, counts):
        return sorted(lst, key=lambda x: (counts[x[0]], x[0]))

    # Step 1: Count occurrences of each identifier
    counts = count_identifiers(lst)

    # Step 2: Sort the list based on identifier and count
    sorted_list = sort_by_count(lst, counts)

    # Step 3: Group the sorted list by identifier
    from itertools import groupby
    grouped = {}
    for key, group in groupby(sorted_list, key=lambda x: x[0]):
        grouped_key = key
        # Collect all elements in the group
        group_list = list(group)
        # Access the second element of the first tuple to determine the group's order
        order_key = group_list[0][1]
        # Append the count and the group's elements
        grouped[grouped_key] = (order_key, group_list + [counts[grouped_key]])

    # Step 4: Sort the groups by count and identifier
    sorted_groups = sorted(grouped.items(), key=lambda x: (x[1][0], x[0]))

    # Step 5: Construct the final list
    result = []
    for group in sorted_groups:
        identifier, (order_key, group_with_order) = group
        result.append((identifier, order_key, group_with_order[0:-1], group_with_order[-1]))

    return result