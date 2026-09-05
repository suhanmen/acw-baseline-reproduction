def count_Substrings(s):
    if not s:
        return 0
    count = 0
    n = len(s)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += int(s[j])
            if current_sum > j - i + 1:
                break  # Optimization: sum can't catch up anymore
            substring_length = j - i + 1
            if current_sum == substring_length:
                count += 1
    return count

# Testing the function with given assertions
assert count_Substrings('112112', 6) == 6, "Test case 1 failed"
assert count_Substrings('111', 3) == 6, "Test case 2 failed"
assert count_Substrings('1101112', 7) == 12, "Test case 3 failed"

print("All assertions passed successfully!")