def neg_count(numbers):
    """
    Counts the number of negative integers in a list.
    """
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count

if __name__ == "__main__":
    assert neg_count([-1, -2, 3, -4, -5]) == 4
    assert neg_count([1, 2, 3]) == 0
    assert neg_count([1, 2, -3, -10, 20]) == 2