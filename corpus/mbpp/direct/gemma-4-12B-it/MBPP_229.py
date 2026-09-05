def re_arrange_array(arr, n):
    res = list(arr)
    for i in range(n):
        if res[i] < 0:
            for j in range(i):
                if res[j] >= 0:
                    res[i], res[j] = res[j], res[i]
                    break
    return res