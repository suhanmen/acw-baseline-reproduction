def total_match(lst1, lst2):
    """
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.
    """
    def char_count(lst):
        return sum(len(s) for s in lst)

    count1 = char_count(lst1)
    count2 = char_count(lst2)

    return lst1 if count1 <= count2 else lst2