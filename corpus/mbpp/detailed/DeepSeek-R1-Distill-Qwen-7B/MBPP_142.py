def count_samepair(list1, list2, list3):
    # Handle empty lists
    if not list1 or not list2 or not list3:
        return 0

    # Create frequency dictionaries for each list
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    count3 = Counter(list3)

    # Find the intersection of all three lists
    common_elements = set(list1) & set(list2) & set(list3)

    # Initialize total pairs counter
    total_pairs = 0

    # Iterate through each common element
    for element in common_elements:
        # Find the minimum count of the element in all lists
        min_count = min(count1[element], count2[element], count3[element])
        # Add to the total pairs
        total_pairs += min_count

    return total_pairs

# Test the function with the given examples
print(count_samepair([1,2,3,4,5,6,7,8], [2,2,3,1,2,6,7,9], [2,1,3,1,2,6,7,9]))  # Output: 3
print(count_samepair([1,2,3,4,5,6,7,8], [2,2,3,1,2,6,7,8], [2,1,3,1,2,6,7,8]))  # Output: 4
print(count_samepair([1,2,3,4,2,6,7,8], [2,2,3,1,2,6,7,8], [2,1,3,1,2,6,7,8]))  # Output: 5