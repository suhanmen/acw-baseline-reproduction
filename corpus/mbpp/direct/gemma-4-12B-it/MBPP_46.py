def test_distinct(numbers):
    """
    Determines whether all numbers in a list are different from each other.

    Args:
        numbers (list): A list of numbers.

    Returns:
        bool: True if all numbers are unique, False otherwise.
    """
    return len(numbers) == len(set(numbers))

if __name__ == "__main__":
    assert test_distinct([1,5,7,9]) == True
    assert test_distinct([2,4,5,5,7,9]) == False
    assert test_distinct([1,2,3]) == True