def counting_sort(arr):
    if not arr:
        return []

    # Find the range of the input array
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    # Create the count array
    count = [0] * range_of_elements

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Construct the sorted array
    sorted_arr = []
    for i in range(range_of_elements):
        # Append the number 'i + min_val' the number of times it appeared
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr