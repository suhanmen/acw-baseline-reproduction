def permute_string(s):
    if not s:
        return []
    result = []
    n = len(s)
    s_list = list(s)
    used = [False] * n

    def permute(index):
        if index == n:
            result.append(''.join(s_list))
            return
        for i in range(n):
            if used[i]:
                continue
            s_list[index], s_list[i] = s_list[i], s_list[index]
            used[i] = True
            permute(index + 1)
            used[i] = False
            s_list[index], s_list[i] = s_list[i], s_list[index]

    permute(0)
    return result

# Test the function with provided assertions
assert permute_string('ab') == ['ab', 'ba']
assert permute_string('abc') == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
assert permute_string('abcd') == ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']