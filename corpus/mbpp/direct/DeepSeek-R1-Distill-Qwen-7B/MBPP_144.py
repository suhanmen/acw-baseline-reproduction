def sum_Pairs(arr, n):
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += abs(arr[i] - arr[j])
    return total