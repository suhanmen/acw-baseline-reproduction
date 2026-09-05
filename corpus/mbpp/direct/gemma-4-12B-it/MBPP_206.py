def concatenate_elements(tuple_input):
    """
    Performs adjacent element concatenation in the given tuples.
    Each resulting element is the concatenation of the current element 
    and the following element in the sequence.
    """
    result = []
    for i in range(len(tuple_input) - 1):
        result.append(tuple_input[i] + tuple_input[i+1])
    return tuple(result)