def get_Inv_Count(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# Test cases
assert get_Inv_Count([1,20,6,4,5],5) == 5
assert get_Inv_Count([1,2,1],3) == 1
assert get_Inv_Count([1,2,5,6,1],5) == 3