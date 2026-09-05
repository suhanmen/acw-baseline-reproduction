def find_minimum_range(arrays):
    import heapq

    if not arrays:
        return (0, 0)  # Handle empty input case

    min Heaps = []
    indices = [0] * len(arrays)
    total_elements = len(arrays[0])
    count = [0] * len(arrays)

    for i in range(len(arrays)):
        heapq.heappush(min Heaps, (arrays[i][0], i, 0))
        count[i] = 1  # Mark the first element as included

    min_range = (float('inf'), float('inf'), float('inf'))  # (max, min, start index)

    while True:
        current_min, current_i, current_pos = heapq.heappop(min Heaps)
        current_max = max(arrays[i][pos] for i, pos in enumerate(indices))
        current_min_val = min(arrays[i][pos] for i, pos in enumerate(indices))

        # Update the global min and max
        if current_max - current_min_val < min_range[0] - min_range[1]:
            min_range = (current_max, current_min_val, current_pos)

        # Move the pointer of the array with the smallest current element
        for i in range(len(arrays)):
            if i == current_i and indices[i] < total_elements:
                indices[i] += 1
                count[i] += 1
                new_val = arrays[i][indices[i]]
                heapq.heappush(min Heaps, (new_val, i, indices[i]))
                break
            elif count[i] < len(arrays[i]):
                continue
            else:
                break  # No more elements to process in this array

    # Extract the result from the min_range tuple
    return (min_range[1], min_range[2])