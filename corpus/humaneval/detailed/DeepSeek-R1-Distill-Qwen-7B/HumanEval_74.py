def total_match(lst1, lst2):
    """
    Write a function that accepts two lists of strings and returns the list that has 
    the total number of chars in all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    """

    def get_total_chars(lst):
        """Helper function to calculate the total number of characters in a list of strings."""
        return sum(len(s) for s in lst)

    total1 = get_total_chars(lst1)
    total2 = get_total_chars(lst2)

    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        return lst1 if len(lst1) != 0 else lst2

    # Handle the case where both totals are zero, or one list is empty
    # If both totals are equal, return the first list, which in the case of empty lists, returns the empty list.