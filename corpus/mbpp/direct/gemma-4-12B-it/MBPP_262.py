def split_two_parts(lst, n):
    """
    Splits a list into two parts where the first part has length n.
    """
    first_part = lst[:n]
    second_part = lst[n:]
    return (first_part, second_part)

if __name__ == "__main__":
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])