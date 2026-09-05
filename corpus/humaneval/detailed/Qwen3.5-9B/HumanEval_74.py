def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''

    # Type check
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError("Both inputs must be lists.")

    # Element type check
    for item in lst1:
        if not isinstance(item, str):
            raise TypeError(f"Expected all elements in lst1 to be strings, got {type(item).__name__}.")
    for item in lst2:
        if not isinstance(item, str):
            raise TypeError(f"Expected all elements in lst2 to be strings, got {type(item).__name__}.")

    # Calculate total character counts
    count1, count2 = calculate_total_char_count(lst1), calculate_total_char_count(lst2)

    # Compare and return
    if count1 < count2:
        return lst1
    elif count2 < count1:
        return lst2
    else:
        return lst1

def calculate_total_char_count(lst):
    '''Helper to sum the length of each string in a list.'''
    total = 0
    for item in lst:
        char_count = len(item)
        total += char_count
    return total