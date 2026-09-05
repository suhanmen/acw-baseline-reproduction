def count_Substring_With_Equal_Ends(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if s[i] == s[j - 1]:
                count += 1
    return count

# Example usage:
print(count_Substring_With_Equal_ENDS('aba'))  # Output: 4
print(count_Substring_With_Equal_ENDS('abcab'))  # Output: 7
print(count_Substring_With_Equal_ENDS('abc'))  # Output: 3