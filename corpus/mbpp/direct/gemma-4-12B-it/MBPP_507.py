def remove_words(words, to_remove):
    """
    Removes specific words from a given list of words.

    Args:
        words (list): The list of strings to filter.
        to_remove (list): The list of strings to be removed.

    Returns:
        list: A new list containing elements from 'words' that are not in 'to_remove'.
    """
    # Using a set for to_remove for O(1) lookup efficiency
    remove_set = set(to_remove)
    return [word for word in words if word not in remove_set]