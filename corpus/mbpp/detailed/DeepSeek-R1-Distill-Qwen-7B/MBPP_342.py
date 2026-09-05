def find_minimum_range(arrays):
    if not arrays or len(arrays) == 0:
        return "Invalid input: empty list of arrays"

    # Check if any array is empty
    for arr in arrays:
        if not arr:
            return "Invalid input: empty array"

    # Find the global min and max across all arrays
    global_min = min(min(arr) for arr in arrays)
    global_max = max(max(arr) for arr in arrays)

    # Dictionary to keep track of the indices of each value
    value_indices = {}
    for arr in arrays:
        for idx, num in enumerate(arr):
            if num not in value_indices:
                value_indices[num] = []
            value_indices[num].append(idx)

    min_range = (global_min, global_max)

    # Current window's min and max pointers
    current_min = global_min
    current_max = global_max

    # Iterate through each unique value as the end of the window
    for end_val in sorted(value_indices.keys()):
        # Update the current window's min and max
        while current_min < end_val:
            # Get all indices where the current min could be updated
            current_min_indices = value_indices.get(current_min, [])
            if current_min_indices:
                for idx in current_min_indices:
                    current_min_idx = idx
                    current_min = arrays[current_min_idx][current_min_idx]
            else:
                # No more possible min values, move to next end_val
                break

        while current_max > end_val:
            # Get all indices where the current max could be updated
            current_max_indices = value_indices.get(current_max, [])
            if current_max_indices:
                for idx in current_max_indices:
                    current_max_idx = idx
                    current_max = arrays[current_max_idx][current_max_idx]
            else:
                # No more possible max values, move to next end_val
                break

        # Check if all arrays have at least one element in the current window
        if current_max - current_min <= 0:
            # Check if all arrays are covered
            covered = True
            for arr in arrays:
                found = False
                for num in arr:
                    if current_min <= num <= current_max:
                        found = True
                        break
                if not found:
                    covered = False
                    break
            if covered:
                if (current_max - current_min) < (min_range[1] - min_range[0]):
                    min_range = (current_min, current_max)

    return min_range