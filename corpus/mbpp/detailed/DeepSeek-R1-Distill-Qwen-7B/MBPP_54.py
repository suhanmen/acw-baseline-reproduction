def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    # If all elements are the same, return the array
    if min_val == max_val:
        return arr

    # Initialize the count array
    range_size = max_val - min_val + 1
    count = [0] * range_size

    # Populate the count array
    for number in arr:
        count[number - min_val] += 1

    # Generate the output array
    output = []
    for i in range(range_size):
        if count[i] > 0:
            output.extend([i + min_val] * count[i])

    return output