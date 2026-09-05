def decode_list(seq):
    result = []
    i = 0
    n = len(seq)
    while i < n:
        if isinstance(seq[i], list) and len(seq[i]) == 2 and isinstance(seq[i][0], int) and seq[i][1] is not None:
            count, value = seq[i]
            if not isinstance(count, int) or count < 0:
                raise ValueError("Invalid run-length pair")
            if isinstance(value, int):
                result.extend([value] * count)
            elif isinstance(value, str):
                result.extend([value] * count)
            else:
                raise TypeError("Value in run-length pair must be int or str")
            i += 2
        else:
            result.append(seq[i])
            i += 1
    return result