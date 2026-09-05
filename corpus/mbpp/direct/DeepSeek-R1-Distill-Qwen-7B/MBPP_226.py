def odd_values_string(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])