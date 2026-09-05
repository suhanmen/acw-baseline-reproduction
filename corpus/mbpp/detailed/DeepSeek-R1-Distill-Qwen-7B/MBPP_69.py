def is_sublist(main_list, sublist):
    # Handle edge cases where sublist is empty or main list is shorter than sublist
    if not sublist:
        return True
    if len(main_list) < len(sublist):
        return False

    # Determine the length of the sublist for comparison
    sublist_length = len(sublist)

    # Iterate through each possible starting index in the main list
    for i in range(len(main_list) - sublist_length + 1):
        # Extract the subsequence from main_list starting at index i
        current_sublist = main_list[i:i+sublist_length]
        # Check if the extracted sublist matches the given sublist
        if current_sublist == sublist:
            return True
    # If no matching sublist found, return False
    return False

# Test the function with the provided examples
assert is_sublist([2,4,3,5,7], [3,7]) == False, "Test case 1 failed"
assert is_sublist([2,4,3,5,7], [4,3]) == True, "Test case 2 failed"
assert is_sublist([2,4,3,5,7], [1,6]) == False, "Test case 3 failed"