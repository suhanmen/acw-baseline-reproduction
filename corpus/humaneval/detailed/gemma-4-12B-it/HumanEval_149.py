from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

    # --- Input Validation ---
    # Ensure the input is a list.
    if not isinstance(lst, list):
        raise ValueError("Input must be a list of strings.")

    # Ensure all elements in the list are strings.
    for item in lst:
        if not isinstance(item, str):
            raise TypeError(f"All elements in the list must be strings. Found: {type(item)}")

    # Handle edge case: Empty input list.
    if not lst:
        return []

    # --- Step 1: Filter out strings with odd lengths ---
    # We create a new list containing only strings where length % 2 == 0.
    filtered_list = []
    for word in lst:
        word_length = len(word)
        if word_length % 2 == 0:
            filtered_list.append(word)

    # Handle edge case: List becomes empty after filtering.
    if not filtered_list:
        return []

    # --- Step 2: Sort the list ---
    # Sorting criteria:
    # 1. Ascending by length of each word.
    # 2. Alphabetically if lengths are equal.

    # We use a stable sort or a composite key.
    # Python's sort is stable, but for clarity and production grade, 
    # a tuple-based key is the standard way to handle multi-level sorting.

    def sorting_key(word: str):
        """
        Returns a tuple representing the priority of sorting.
        Primary key: length of the string.
        Secondary key: alphabetical order of the string.
        """
        word_length = len(word)
        return (word_length, word)

    # We sort the filtered list in place or return a new sorted list.
    # Using sorted() ensures we don't mutate the intermediate filtered_list
    # if we want to be strictly safe, though here it's a local variable.
    sorted_result = sorted(filtered_list, key=sorting_key)

    return sorted_result

# Example of how the logic behaves:
# list_sort(["aa", "a", "aaa"]) -> filtered: ["aa"] -> sorted: ["aa"]
# list_sort(["ab", "a", "aaa", "cd"]) -> filtered: ["ab", "cd"] -> sorted: ["ab", "cd"]