def find_adverb_position(sentence):
    adverbs = []
    adverb_positions = []

    # Iterate through each character in the sentence
    for i, char in enumerate(sentence):
        # Check if the character is an apostrophe followed by 'ly' in lowercase
        if char == "'" and i >= 2:
            if sentence[i-1:i+1] == "'ly'" and i >= 2 and i < len(sentence)-1:
                adverbs.append(sentence[i-2:i+1])
                adverb_positions.append((i-2, i, sentence[i-2:i+1]))

    # Return the adverbs and their positions if found
    if adverbs:
        return adverb_positions
    else:
        return []

# Example usage:
# assert find_adverb_position("clearly!! we can see the sky") == [(0, 7, 'clearly')]
# assert find_adverb_position("seriously!! there are many roses") == [(0, 9, 'seriously')]
# assert find_adverb_position("unfortunately!! sita is going to home") == [(0, 13, 'unfortunately')]