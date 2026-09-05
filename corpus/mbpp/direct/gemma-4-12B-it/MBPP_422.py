def find_Average_Of_Cube(n):
    """
    Finds the average of cubes of the first n natural numbers.
    The sum of cubes of the first n natural numbers is given by:
    (n * (n + 1) / 2)^2
    The average is this sum divided by n.
    """
    if n <= 0:
        return 0

    # Mathematical formula for sum of cubes: [n(n+1)/2]^2
    total_sum = (n * (n + 1) // 2) ** 2
    average = total_sum / n
    return average

if __name__ == "__main__":
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1