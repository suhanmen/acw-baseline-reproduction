from fractions import Fraction

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
    try:
        # Convert the fractions from string format to Fraction objects
        x_fraction = Fraction(x.split('/')[0], x.split('/')[1])
        n_fraction = Fraction(n.split('/')[0], n.split('/')[1])

        # Multiply the two fractions
        product = x_fraction * n_fraction

        # Check if the product is an integer
        return product.denominator == 1
    except:
        return False