def get_row(lst, x):
    result = []
    for row_idx, row in enumerate(lst):
        for col_idx, num in enumerate(row):
            if num == x:
                result.append((row_idx, col_idx))
    # Sort first by row ascending, then by column descending within the row
    result.sort(key=lambda item: (item[0], -item[1]))
    return result