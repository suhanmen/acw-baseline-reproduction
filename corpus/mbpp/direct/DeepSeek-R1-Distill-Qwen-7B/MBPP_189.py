def first_Missing_Positive(arr, max_num):
    positives = {x for x in arr if x > 0}
    for i in range(1, max_num + 1):
        if i not in positives:
            return i
    return max_num + 1 if max_num > 0 else 1