def sum_Of_Series(n: int) -> int:
    """
    Calculates the sum of the cubes of the first n natural numbers.
    The formula for the sum of cubes is (n * (n + 1) / 2)^2.
    """
    return (n * (n + 1) // 2) ** 2

if __name__ == "__main__":
    assert sum_Of_Series(5) == 225
    assert sum_Of_Series(2) == 9
    assert sum_Of_Series(3) == 36