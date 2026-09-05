def add_lists(lst: list, tpl: tuple) -> tuple:
    """
    Appends a list to a tuple and returns the resulting tuple.
    """
    return tpl + tuple(lst)

if __name__ == "__main__":
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)