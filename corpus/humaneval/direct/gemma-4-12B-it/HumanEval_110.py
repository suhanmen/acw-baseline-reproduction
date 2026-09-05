def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Identify how many odd numbers are currently in lst1
    odd_in_lst1 = [x for x in lst1 if x % 2 != 0]
    # Identify how many even numbers are available in lst2 to replace the odd ones in lst1
    even_in_lst2 = [x for x in lst2 if x % 2 == 0]

    # If the number of odd numbers in lst1 is less than or equal to the 
    # number of even numbers available in lst2, we can swap them all.
    if len(odd_in_lst1) <= len(even_in_lst2):
        return "YES"
    else:
        return "NO"