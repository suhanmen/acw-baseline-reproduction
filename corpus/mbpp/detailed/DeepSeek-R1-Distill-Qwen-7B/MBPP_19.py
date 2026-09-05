def test_duplicate(arr):
    # Check for edge cases with an empty array or single element
    if len(arr) < 2:
        return False

    # Helper function to check for duplicates
    def contains_duplicate(sub_arr):
        # Early exit if duplicates are found
        for num in sub_arr:
            if num in sub_arr[:i]:
                return True
            # Check if the current number is already in the set
            if num in seen:
                return True
            # Add the number to the set
            seen.add(num)
        return False

    # Create a set to track unique elements
    seen = set()
    for i, num in enumerate(arr):
        # Early exit if the array is already longer than possible unique elements
        if len(arr) - i <= len(seen):
            return True
        # Add the current number to the set
        seen.add(num)
        # Check if the current number has been seen before
        if num in seen:
            return True
    # If no duplicates found
    return False