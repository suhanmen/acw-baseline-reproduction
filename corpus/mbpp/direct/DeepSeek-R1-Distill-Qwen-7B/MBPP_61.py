def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += int(s[j])
            if current_sum == (j - i + 1):
                count += 1
    return count

# Test cases
assert count_Substrings('112112', 6) == 6
assert count_Substrings('111', 3) == 6
assert count_Substrings('1101112', 7) == 12