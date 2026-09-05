def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated[-1] == '1':
            count += 1
    return count