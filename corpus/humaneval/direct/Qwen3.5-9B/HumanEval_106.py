def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    result = []
    factorial = 1
    total_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            # i is even: compute factorial of i
            # Since we iterate sequentially, we can maintain factorial incrementally
            factorial *= i
            result.append(factorial)
        else:
            # i is odd: compute sum from 1 to i
            total_sum += i
            result.append(total_sum)
    return result