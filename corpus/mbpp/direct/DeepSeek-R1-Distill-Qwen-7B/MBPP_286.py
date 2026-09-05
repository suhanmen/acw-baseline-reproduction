def max_sub_array_sum_repeated(arr, k):
    def kadane_algorithm(sub_arr):
        max_current = max_global = sub_arr[0]
        for num in sub_arr[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global

    max_single = kadane_algorithm(arr)
    total = sum(arr)
    max_total = total * k

    if total > 0:
        max_sub = max(max_single, max_total)
    else:
        max_sub = max_single

    if max_sub < 0:
        max_sub = max(arr)

    return max_sub