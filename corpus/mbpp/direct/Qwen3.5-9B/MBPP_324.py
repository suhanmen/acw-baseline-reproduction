from itertools import groupby

def sum_of_alternates(tuple_input):
    # Convert input to list for indexing
    lst = list(tuple_input)
    n = len(lst)

    # Calculate sum of elements at even indices (0, 2, 4, ...)
    even_sum = 0
    for i in range(0, n, 2):
        even_sum += lst[i]

    # Calculate sum of elements at odd indices (1, 3, 5, ...)
    odd_sum = 0
    for i in range(1, n, 2):
        odd_sum += lst[i]

    return (even_sum, odd_sum)