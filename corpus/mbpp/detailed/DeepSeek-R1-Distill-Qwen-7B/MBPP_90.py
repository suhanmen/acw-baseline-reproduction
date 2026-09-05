def len_log(words):
    def is_valid_list(w):
        if not isinstance(w, list):
            return False, "Invalid input: not a list"
        for item in w:
            if not isinstance(item, str):
                return False, "Invalid input: non-string element"
        return True, None

    valid, error = is_valid_list(words)
    if not valid:
        raise ValueError(error)

    def get_max_length(word_list):
        if not word_list:
            return 0
        max_length = 0
        for word in word_list:
            current_length = len(word)
            if current_length > max_length:
                max_length = current_length
        return max_length

    return get_max_length(words)