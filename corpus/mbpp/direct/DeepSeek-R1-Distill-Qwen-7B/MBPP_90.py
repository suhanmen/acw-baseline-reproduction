def len_log(words):
    max_length = 0
    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length
    return max_length