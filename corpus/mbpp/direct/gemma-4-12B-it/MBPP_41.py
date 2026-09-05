def filter_evennumbers(numbers):
    """
    Filters even numbers from a list using a lambda function.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    assert filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]
    assert filter_evennumbers([10, 20, 45, 67, 84, 93]) == [10, 20, 84]
    assert filter_evennumbers([5, 7, 9, 8, 6, 4, 3]) == [8, 6, 4]