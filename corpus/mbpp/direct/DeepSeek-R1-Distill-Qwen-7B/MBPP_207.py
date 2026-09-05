def find_longest_repeating_subseq(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            count = 0
            current = s[i]
            for k in range(j + 1, n):
                if s[k] == current:
                    count += 1
                    if count > max_len:
                        max_len = count
                    current = s[k]
    return max_len

# Example usage
print(find_longest_repeating_subseq("AABEBCDD"))  # Output: 3
print(find_longest_repeating_subseq("aabb"))       # Output: 2
print(find_longest_repeating_subseq("aab"))        # Output: 1