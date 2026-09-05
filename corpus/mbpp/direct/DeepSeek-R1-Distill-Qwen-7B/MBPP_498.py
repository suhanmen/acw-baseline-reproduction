def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# These assertions are given as examples of usage, but the problem statement does not require testing these specific cases.
# To test this function, you can use:
# 
# assert gcd(12, 17) == 1
# assert gcd(4,6) == 2
# assert gcd(2,9) == 1