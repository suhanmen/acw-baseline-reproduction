def text_match_word(s):
    if not s.strip():
        return 'Not matched!'

    trimmed_s = s.strip()
    word_end = trimmed_s.find(' ')
    if word_end == -1:
        word_part = trimmed_s
        punctuation_part = ''
    else:
        word_part = trimmed_s[:word_end]
        punctuation_part = trimmed_s[word_end:]

    if not word_part:
        return 'Not matched!'

    valid_punctuation = set('!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~')
    if any(c not in valid_punctuation for c in punctuation_part):
        return 'Not matched!'

    if word_part == trimmed_s:
        return 'Found a match!'
    else:
        return 'Not matched!'