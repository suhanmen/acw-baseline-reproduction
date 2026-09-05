def concatenate_tuple(input_tuple, delimiter="-"):
    """
    Concatenates each element of a tuple into a single string 
    separated by a specified delimiter. Non-string elements 
    are converted to strings first.
    """
    return delimiter.join(map(str, input_tuple))

if __name__ == "__main__":
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'