def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    def parse_fraction(fraction_str):
        numerator_str, denominator_str = fraction_str.split('/')
        return int(numerator_str), int(denominator_str)

    def is_valid_fraction(fraction_str):
        numerator, denominator = parse_fraction(fraction_str)
        return denominator != 0 and numerator > 0 and denominator > 0

    x_num, x_den = parse_fraction(x)
    n_num, n_den = parse_fraction(n)

    if not (is_valid_fraction(x) and is_valid_fraction(n)):
        raise ValueError("Invalid fraction format")

    # Multiply the two fractions: (x_num / x_den) * (n_num / n_den) = (x_num * n_num) / (x_den * n_den)
    total_numerator = x_num * n_num
    total_denominator = x_den * n_den

    # Check if total_numerator is divisible by total_denominator
    return total_numerator % total_denominator == 0