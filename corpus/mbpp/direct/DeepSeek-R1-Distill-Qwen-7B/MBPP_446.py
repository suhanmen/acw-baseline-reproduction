def count_Occurrence(tuple_, list_):
    # Count the occurrences of each element in list_ that are present in tuple_
    count = 0
    for element in list_:
        if element in tuple_:
            count += tuple_.count(element)
    return count

# Example usage:
# count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) returns 3
# count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]) returns 6
# count_Occurrence((1,2,3,4,5,6), [1,2]) returns 2