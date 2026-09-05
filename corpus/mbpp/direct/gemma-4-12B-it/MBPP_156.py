def tuple_int_str(data):
    """
    Converts a nested tuple of string values to a nested tuple of integer values.
    """
    result = []
    for inner_tuple in data:
        # Convert each string in the inner tuple to an integer
        converted_inner = tuple(int(item) for item in inner_tuple)
        result.append(converted_inner)
    return tuple(result)

if __name__ == "__main__":
    assert tuple_int_str((('333', '33'), ('1416', '55'))) == ((333, 33), (1416, 55))
    assert tuple_int_str((('999', '99'), ('1000', '500'))) == ((999, 99), (1000, 500))
    assert tuple_int_str((('666', '66'), ('1500', '555'))) == ((666, 66), (1500, 555))