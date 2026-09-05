def concatenate_elements(lst):
    if not lst:
        return ''
    space_count = 0
    result = lst[0]
    for word in lst[1:]:
        result += ' ' * space_count + word
        space_count = len(word) > 1
    return result