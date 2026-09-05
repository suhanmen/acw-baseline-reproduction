def add_nested_tuples(tuple1, tuple2):
    """
    Performs index-wise addition of elements in two nested tuples.
    """
    result = []
    for i in range(len(tuple1)):
        inner_tuple1 = tuple1[i]
        inner_tuple2 = tuple2[i]
        # Perform addition for each element in the nested tuple
        added_inner = tuple(a + b for a, b in zip(inner_tuple1, inner_tuple2))
        result.append(added_inner)

    return tuple(result)

if __name__ == "__main__":
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))