from math import gcd

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
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))

    # Product: (num_x * num_n) / (den_x * den_n)
    # Result is whole number if (num_x * num_n) % gcd(den_x * den_n, num_x * num_n) == 0
    # Simpler: after multiplying, the result is integer iff (den_x * den_n) divides (num_x * num_n)
    # But we can reduce before checking: 
    # Let g = gcd(den_x, num_n), then den_x becomes den_x/g, num_n becomes num_n*g
    # Then check if remaining denominator divides numerator.

    # More direct: compute product numerator and denominator, then check divisibility
    prod_num = num_x * num_n
    prod_den = den_x * den_n

    # Check if prod_den divides prod_num
    return prod_num % prod_den == 0