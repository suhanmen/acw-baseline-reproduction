def positive_count(arr):
    if len(arr) == 0:
        return 0.0
    positive = sum(1 for x in arr if x > 0)
    return positive / len(arr)