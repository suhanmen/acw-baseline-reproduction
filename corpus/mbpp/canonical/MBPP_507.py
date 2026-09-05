def remove_words(list1, removewords):
    for word in list(list1):
        if word in removewords:
            list1.remove(word)
    return list1  