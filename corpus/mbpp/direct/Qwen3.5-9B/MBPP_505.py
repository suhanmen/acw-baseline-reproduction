def re_order(arr):
    non_zero = [x for x in arr if x != 0]
    return non_zero + [0] * (len(arr) - len(non_zero))