def greater_specificnum(lst, specific_num):
    # Step 1: Validate inputs
    if not isinstance(lst, list) or not isinstance(specific_num, int):
        return False

    # Step 2: Initialize a list to hold values greater than specific_num
    greater_values = []

    # Step 3: Iterate through each element in the list
    for value in lst:
        # Check if current value is greater than specific_num
        if isinstance(value, int) and value > specific_num:
            greater_values.append(value)

    # Step 4: Determine if there are any values greater than specific_num
    return len(greater_values) > 0

# Step 5: Test the function with the provided examples
assert greater_specificnum([220, 330, 500], 200) == True, "Test case 1 failed"
assert greater_specificnum([12, 17, 21], 20) == False, "Test case 2 failed"
assert greater_specificnum([1, 2, 3, 4], 10) == False, "Test case 3 failed"