def Find_Min_Length(sublists):
    if not sublists:
        return 0
    min_length = float('inf')
    for sublist in sublists:
        if not sublist:
            return 0
        current_length = len(sublist)
        if current_length < min_length:
            min_length = current_length
    return min_length