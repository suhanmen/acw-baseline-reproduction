def positive_count(arr):
    positive = 0
    total = len(arr)
    for num in arr:
        if num > 0:
            positive += 1
    return positive / total