def pos_count(numbers: list) -> int:
    """
    Counts the number of positive integers in a given list.
    """
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

if __name__ == "__main__":
    assert pos_count([1, -2, 3, -4]) == 2
    assert pos_count([3, 4, 5, -1]) == 3
    assert pos_count([1, 2, 3, 4]) == 4