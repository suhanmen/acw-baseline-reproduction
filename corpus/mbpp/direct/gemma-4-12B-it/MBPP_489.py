def frequency_Of_Largest(size, arr):
    if not arr:
        return 0

    max_val = max(arr)
    count = 0
    for num in arr:
        if num == max_val:
            count += 1
    return count

if __name__ == "__main__":
    assert frequency_Of_Largest(5, [1, 2, 3, 4, 4]) == 2
    assert frequency_Of_Largest(3, [5, 6, 5]) == 1
    assert frequency_Of_Largest(4, [2, 7, 7, 7]) == 3