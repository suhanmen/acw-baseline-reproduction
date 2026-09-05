def Extract(lst):
    # Handle empty input
    if not lst:
        return []

    result = []
    for sublist in lst:
        # Handle empty sublist by appending None
        if not sublist:
            result.append(None)
        else:
            # Append the first element of the sublist
            result.append(sublist[0])
    return result

# Test the function with provided examples
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6], "Test case 1 failed"
assert Extract([[1,2,3],[4, 5]]) == [1,4], "Test case 2 failed"
assert Extract([[9,8,1],[1,2]]) == [9,1], "Test case 3 failed"

print("All test cases passed successfully!")