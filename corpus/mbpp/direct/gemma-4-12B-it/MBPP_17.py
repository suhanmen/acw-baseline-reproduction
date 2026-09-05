def square_perimeter(side_length):
    """
    Calculates the perimeter of a square given the length of one side.

    Args:
        side_length (int/float): The length of one side of the square.

    Returns:
        int/float: The perimeter of the square.
    """
    return 4 * side_length

if __name__ == "__main__":
    assert square_perimeter(10) == 40
    assert square_perimeter(5) == 20
    assert square_perimeter(4) == 16