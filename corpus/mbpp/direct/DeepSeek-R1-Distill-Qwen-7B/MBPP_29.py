def get_Odd_Occurrence(arr):
    odd_count = {}
    for num in arr:
        if num in odd_count:
            odd_count[num] ^= 1
        else:
            odd_count[num] = 1
    for key, value in odd_count.items():
        if value == 1:
            return key
    return -1  # This return is just to satisfy the function signature, it won't be reached with the problem constraints.