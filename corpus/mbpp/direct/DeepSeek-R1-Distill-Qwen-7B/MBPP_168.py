def frequency(arr, num):
    count = 0
    for num_in in arr:
        if num_in == num:
            count += 1
    return count