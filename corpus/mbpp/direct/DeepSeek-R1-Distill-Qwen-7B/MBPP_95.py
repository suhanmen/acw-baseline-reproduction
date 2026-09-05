def Find_Min_Length(all_lists):
    min_length = float('inf')
    for lst in all_lists:
        if not lst:
            continue
        current_length = 1
        prev = lst[0]
        for num in lst[1:]:
            if num == prev:
                current_length += 1
            else:
                if current_length < min_length:
                    min_length = current_length
                current_length = 1
                prev = num
        # Check after loop in case the last elements were same
        if current_length < min_length:
            min_length = current_length
    return min_length