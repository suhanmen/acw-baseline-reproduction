def search(lst):
    from collections import Counter
    counts = Counter(lst)
    max_num = -1
    for num in counts:
        if counts[num] >= num and num > 0:
            if num > max_num:
                max_num = num
    return max_num if max_num != -1 else -1