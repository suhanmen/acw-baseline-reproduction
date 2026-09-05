def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n, are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    def parse_fraction(f_str):
        num_str, den_str = f_str.split('/')
        return int(num_str), int(den_str)

    num_x, den_x = parse_fraction(x)
    num_n, den_n = parse_fraction(n)

    # x * n = (num_x * num_n) / (den_x * den_n)
    # A fraction is a whole number if the numerator is divisible by the denominator.
    numerator_total = num_x * num_n
    denominator_total = den_x * den_n

    return numerator_total % denominator_total == 0