def first_element(arr, k, limit):
    if k <= 0 or k > limit:
        raise ValueError("k must be positive and at most the length of the array")

    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
        if count[num] == k:
            return num
    return None