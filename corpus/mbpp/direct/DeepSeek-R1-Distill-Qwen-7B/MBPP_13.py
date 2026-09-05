def count_common(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Sort the dictionary items by count in descending order
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words

# Test cases to verify the function
assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
assert count_common(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
assert count_common(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]