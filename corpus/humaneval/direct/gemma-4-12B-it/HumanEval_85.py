def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    # Iterate through the list starting from index 1 (odd index), 
    # stepping by 2 to target all odd indices (1, 3, 5, ...)
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total