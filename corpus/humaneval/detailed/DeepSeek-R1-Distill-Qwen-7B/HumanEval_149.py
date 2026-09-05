def sorted_list_sum(lst):
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
    # Step 1: Filter out strings with odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]

    # Step 2: Sort the filtered list by length, then alphabetically
    # First, sort by length
    sorted_by_length = sorted(filtered, key=lambda x: len(x))

    # If all lengths are the same, return the list sorted alphabetically
    # To check if all lengths are the same:
    if len(set(len(s) for s in filtered)) == 1:
        sorted_list = sorted(sorted_by_length, key=lambda x: x)
    else:
        # If lengths are not all the same, sort by both length and then by the string
        sorted_list = sorted(sorted_by_length, key=lambda x: (len(x), x))

    # Handle edge cases
    if not filtered:
        return []
    if len(filtered) == 1:
        return filtered

    # Final check: If all strings have even lengths, proceed; else, return empty list
    if all(len(s) % 2 == 0 for s in lst):
        return sorted_list
    else:
        return []