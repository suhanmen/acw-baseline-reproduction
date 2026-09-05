def find_adverb_position(sentence):
    words = sentence.split()
    adverbs = []

    for word in words:
        if len(word) >= 2 and word.endswith('!!'):
            adverbs.append(word)

    if not adverbs:
        return None

    first_adverb = adverbs[0]
    start_index = sentence.index(first_adverb)
    end_index = start_index + len(first_adverb)

    return (start_index, end_index, first_adverb)