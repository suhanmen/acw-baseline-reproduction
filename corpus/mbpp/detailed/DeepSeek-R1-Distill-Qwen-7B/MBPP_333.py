def Sort(lst):
    """Sort a list of sublists based on the second element of each sublist."""
    # Handle empty list
    if not lst:
        return []

    # Handle single-element list
    if len(lst) == 1:
        return lst

    # Extract the second elements of each sublist for sorting
    second_elements = [sublist[1] for sublist in lst]

    # Determine the desired order (ascending by default)
    ascending = True

    # If the second elements are all equal, sorting is irrelevant but enforce an order
    if len(set(second_elements)) == 1:
        # Return the original list to maintain order
        return lst.copy()

    # Sort the sublists based on the second elements
    # Using explicit comparison logic for stability
    sorted_sublists = []
    for i in range(len(lst)):
        min_sub = lst[i]
        for j in range(i + 1, len(lst)):
            # Compare current min_sub with lst[j]
            if (ascending and 
                second_elements[second_elements.index(min_sub[1])] >= 
                second_elements[second_elements.index(lst[j][1])]) or \
                (not ascending and 
                second_elements[second_elements.index(min_sub[1])] <= 
                second_elements[second_elements.index(lst[j][1])]):
                min_sub = lst[j]
        sorted_sublists.append(min_sub)

    return sorted_sublists

# Test cases to verify the correctness of the function
def test_sort_function():
    assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]
    assert Sort([['452', 10], ['256', 5], ['100', 20], ['135', 15]]) == [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
    assert Sort([['rishi', 10], ['akhil', 5], ['ramya', 20], ['gaur', 15]]) == [['akhil', 5], ['rishi', 10], ['gaur', 15], ['ramya', 20]]
    print("All test cases passed successfully.")

test_sort_function()