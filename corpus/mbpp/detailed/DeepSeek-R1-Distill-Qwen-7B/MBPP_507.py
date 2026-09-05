def remove_words(all_words, words_to_remove=None):
    """
    Remove specific words from a given list and return the modified list.

    Args:
        all_words (list): The list of words to process.
        words_to_remove (list, optional): The list of words to remove from all_words. Defaults to None.

    Returns:
        list: A new list containing words from all_words that are not in words_to_remove.

    Raises:
        TypeError: If either all_words or words_to_remove is not a list.
    """
    # Validate inputs
    if not isinstance(all_words, list):
        raise TypeError("all_words must be a list.")
    if words_to_remove is not None and not isinstance(words_to_remove, list):
        raise TypeError("words_to_remove must be a list.")

    # Handle the case where words_to_remove is None
    if words_to_remove is None:
        words_to_remove = set()

    # Convert words_to_remove to a set for efficient lookups
    remove_set = set(words_to_remove)

    # Filter the all_words list, including only words not in remove_set
    result = [word for word in all_words if word not in remove_set]

    return result