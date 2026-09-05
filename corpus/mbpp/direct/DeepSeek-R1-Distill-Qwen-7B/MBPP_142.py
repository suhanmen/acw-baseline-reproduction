def count_samepair(list1, list2, list3):
    count = 0
    # Create a frequency dictionary for list1
    freq1 = {}
    for num in list1:
        freq1[num] = freq1.get(num, 0) + 1
    # Create a frequency dictionary for list2
    freq2 = {}
    for num in list2:
        freq2[num] = freq2.get(num, 0) + 1
    # Create a frequency dictionary for list3
    freq3 = {}
    for num in list3:
        freq3[num] = freq3.get(num, 0) + 1
    # Iterate through all unique numbers in list1 and list2
    all_nums = set(freq1.keys()).union(set(freq2.keys())).union(set(freq3.keys()))
    for num in all_nums:
        # Check if the number exists in all three lists
        if num in freq1 and num in freq2 and num in freq3:
            # Calculate the minimum count among the three lists
            min_count = min(freq1[num], freq2[num], freq3[num])
            # Add the minimum count to the total count
            count += min_count
    return count