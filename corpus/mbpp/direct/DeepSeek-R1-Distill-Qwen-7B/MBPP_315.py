def find_Max_Len_Even(s):
    words = s.split()
    max_len = -1
    for word in words:
        if len(word) % 2 == 0 and len(word) > max_len:
            max_len = len(word)
    return max_len if max_len != 0 else '-1'