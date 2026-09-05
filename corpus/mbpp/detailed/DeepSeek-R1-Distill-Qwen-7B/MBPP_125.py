def find_length(binary_string):
    # Handle empty input
    if not binary_string:
        return 0

    # Initialize variables to track the maximum difference
    max_diff = -1
    n = len(binary_string)

    # Iterate over all possible starting indices
    for i in range(n):
        # Count 0s and 1s starting from index i
        count_0 = 0
        count_1 = 0
        for j in range(i, n):
            if binary_string[j] == '0':
                count_0 += 1
            else:
                count_1 += 1
            # Calculate the current difference
            current_diff = abs(count_0 - count_1)
            # Update the maximum difference if current is higher
            if current_diff > max_diff:
                max_diff = current_diff

    # Handle the case where the entire string is 0s or 1s
    if max_diff == -1:
        # This can happen if the string is empty, which we've already handled
        pass
    else:
        # Check if the maximum difference is the length of the string
        if max_diff == 0:
            # All characters are the same, so the maximum difference is the length
            max_diff = n

    return max_diff if max_diff != -1 else 0

# Test cases
assert find_length("11000010001", 11) == 6
assert find_length("10111", 5) == 1
assert find_length("11011101100101", 14) == 2

print("All test cases passed.")