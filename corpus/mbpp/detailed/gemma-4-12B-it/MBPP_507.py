from typing import List


def remove_words(input_list: List[str], words_to_remove: List[str]) -> List[str]:
    """
    Removes specific words from a list of words.

    Args:
        input_list (List[str]): The original list of strings.
        words_to_remove (List[str]): A list of strings that should be removed from the input_list.

    Returns:
        List[str]: A new list containing only the words not present in the words_to_remove list.

    Raises:
        TypeError: If input_list or words_to_remove are not lists.
        AttributeError: If elements in the lists are not strings.
    """
    # Defensive Programming: Validate input types
    if not isinstance(input_list, list):
        raise TypeError(f"Expected input_list to be a list, but got {type(input_list).__name__}")

    if not isinstance(words_to_remove, list):
        raise TypeError(f"Expected words_to_remove to be a list, but got {type(words_to_remove).__name__}")

    # Defensive Programming: Validate internal element types
    _validate_list_contents(input_list, "input_list")
    _validate_list_contents(words_to_remove, "words_to_remove")

    # Edge Case: If the input list is empty, return an empty list immediately.
    if not input_list:
        return []

    # Edge Case: If the removal list is empty, return a copy of the original list.
    if not words_to_remove:
        return list(input_list)

    # Optimization: Convert the list of words to remove into a set for O(1) average lookup.
    # This ensures the algorithm runs in O(N + M) time rather than O(N * M).
    removal_set = set(words_to_remove)

    # Construct the result list
    # We use a list comprehension or explicit loop to maintain the relative order of elements.
    result_list = []
    for word in input_list:
        # Check if the current word exists in the removal set
        should_remove = word in removal_set

        if not should_remove:
            # If the word is not in the removal set, we keep it.
            result_list.append(word)

    return result_list


def _validate_list_contents(data: List[str], name: str) -> None:
    """
    Helper function to ensure all elements in a list are strings.
    """
    for index, item in enumerate(data):
        if not isinstance(item, str):
            raise AttributeError(
                f"Element at index {index} in {name} is of type {type(item).__name__}, "
                "but only strings are allowed."
            )


if __name__ == "__main__":
    # The following assertions verify the requirements provided in the problem description.
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'], ['white', 'orange']) == ['red', 'green', 'blue', 'black']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'], ['black', 'orange']) == ['red', 'green', 'blue', 'white']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'], ['blue', 'white']) == ['red', 'green', 'black', 'orange']