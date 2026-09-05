def index_multiplication(tuple1, tuple2):
    """
    Perform index-wise multiplication of tuple elements in the given two tuples.
    The input is a tuple of tuples, and the output is a tuple of tuples.
    """
    result = []
    for t1, t2 in zip(tuple1, tuple2):
        # Multiply corresponding elements of the inner tuples
        multiplied_tuple = tuple(x * y for x, y in zip(t1, t2))
        result.append(multiplied_tuple)

    return tuple(result)

if __name__ == "__main__":
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((24, 45), (30, 77), (12, 33), (27, 60))