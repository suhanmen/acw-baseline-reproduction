def sort_mixed_list(lst):
    """
    Sorts a mixed list of integers and strings.
    Integers are sorted numerically first, followed by strings alphabetically.
    """
    # Separate the list into two groups
    integers = sorted([x for x in lst if isinstance(x, int)])
    strings = sorted([x for x in lst if isinstance(x, str)])

    # Combine and return
    return integers + strings

if __name__ == "__main__":
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']