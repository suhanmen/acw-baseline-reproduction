def remove_column(lst, col):
    return [row[:col] + row[col+1:] for row in lst]