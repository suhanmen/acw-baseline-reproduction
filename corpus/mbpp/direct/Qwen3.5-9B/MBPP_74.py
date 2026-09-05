def is_samepatterns(words, patterns):
    if len(words) != len(patterns):
        return False
    n = len(words)
    word_to_pattern = {}
    pattern_to_word = {}
    for i in range(n):
        w, p = words[i], patterns[i]
        if w in word_to_pattern:
            if word_to_pattern[w] != p:
                return False
        else:
            word_to_pattern[w] = p
        if p in pattern_to_word:
            if pattern_to_word[p] != w:
                return False
        else:
            pattern_to_word[p] = w
    return True