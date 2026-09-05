def count_Substring_With_Equal_Ends(s):
    if not s:
        return 0

    count = 0
    length = len(s)

    for i in range(length):
        for j in range(i, length):
            substring = s[i:j+1]
            if substring[0] == substring[-1]:
                count += 1

    return count