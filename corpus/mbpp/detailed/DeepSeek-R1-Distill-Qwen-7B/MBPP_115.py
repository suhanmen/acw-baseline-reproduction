def empty_dit(arr):
    # Check if the input is an empty list
    if not arr:
        return True

    # Iterate through each element in the list
    for d in arr:
        # Check if the current dictionary is empty
        if d:
            return False

    # If all dictionaries are empty, return True
    return True