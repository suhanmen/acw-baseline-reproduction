def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def compute_factorial(i):
        """Helper function to compute the factorial of i."""
        if i < 0:
            raise ValueError("Factorial of negative number is undefined.")
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        return factorial

    def compute_sum(i):
        """Helper function to compute the sum of numbers from 1 to i."""
        return i * (i + 1) // 2

    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("n cannot be negative.")

    # Handle the case when n is zero or negative (already validated above)
    if n == 0:
        return []

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(compute_factorial(i))
        else:
            result.append(compute_sum(i))

    return result