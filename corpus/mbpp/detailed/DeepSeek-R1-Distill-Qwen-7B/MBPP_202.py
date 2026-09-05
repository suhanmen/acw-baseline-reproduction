def remove_even(s):
    result = []
    for index, char in enumerate(s):
        if index % 2 == 0:
            result.append(char)
    return ''.join(result)