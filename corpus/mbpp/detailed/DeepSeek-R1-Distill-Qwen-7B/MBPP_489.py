def frequency_of_largest(frequency, arr):
    if not arr:
        return 0
    largest = max(arr)
    frequency = arr.count(largest)
    return frequency