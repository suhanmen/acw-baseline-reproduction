def sum_difference(n: int) -> int:
    """
    Calculates the difference between the squared sum of the first n 
    natural numbers and the sum of the squared first n natural numbers.

    Formulae:
    Sum of first n numbers: S = n(n + 1) / 2
    Squared sum: S^2 = (n(n + 1) / 2)^2
    Sum of squares: SS = n(n + 1)(2n + 1) / 6
    Difference: S^2 - SS
    """
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2
    squared_sum = sum_n ** 2

    # Calculate the sum of the squares of the first n natural numbers
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    return squared_sum - sum_of_squares