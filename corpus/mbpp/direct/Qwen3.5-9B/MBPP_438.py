def count_bidirectional(lst):
    seen = set()
    count = 0
    for a, b in lst:
        pair = (a, b)
        reverse = (b, a)
        if reverse in seen or (pair in seen and reverse in seen):
            pass  # Already counted
        elif pair not in seen:
            if reverse in seen:
                count += 1
            seen.add(pair)
    return count

# To ensure the function returns strings as per assertions, wrap in str()
def count_bidirectional(lst):
    seen = set()
    count = 0
    for a, b in lst:
        pair = (a, b)
        reverse = (b, a)
        if pair in seen and reverse in seen:
            pass  # Already counted
        elif pair not in seen:
            if reverse in seen:
                count += 1
            seen.add(pair)
    return str(count)