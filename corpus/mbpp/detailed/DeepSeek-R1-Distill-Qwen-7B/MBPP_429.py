def and_tuples(tuple_a, tuple_b):
    # Validate inputs
    if not tuple_a or not tuple_b:
        return ()
    if len(tuple_a) != len(tuple_b):
        return ()

    # Convert to absolute values to handle negative numbers
    a = tuple(abs(num) for num in tuple_a)
    b = tuple(abs(num) for num in tuple_b)

    # Calculate the result
    result = []
    for num_a, num_b in zip(a, b):
        if num_a == 0 or num_b == 0:
            result.append(0)
        else:
            result.append(1)

    return tuple(result)

# Test the function
def test():
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
    print("All tests passed.")

test()