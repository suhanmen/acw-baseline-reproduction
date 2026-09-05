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
    def count_even_odd(lst):
        even = 0
        odd = 0
        for num in lst:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        return even, odd

    even1, odd1 = count_even_odd(lst1)
    even2, odd2 = count_even_odd(lst2)

    if even1 == 0:
        return "NO"

    required = odd1
    available_even = even2

    if required > available_even:
        return "NO"

    # Check if lst2 can provide enough odds or if lst1 can provide even to swap
    if odd2 > 0 and even1 > 0:
        # Swap one odd from lst1 with one even from lst2
        return "YES"
    else:
        # lst2 has no odds or lst1 has no evens to swap, can lst2 fill the needed evens?
        if available_even >= required:
            return "YES"
        else:
            return "NO"