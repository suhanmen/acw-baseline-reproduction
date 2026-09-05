import math

def is_woodall(n: int) -> bool:
    """
    A Woodall number is a natural number of the form W_n = n * 2^n - 1.
    This function checks if a given number n is a Woodall number.
    """
    if n < 1:
        return False

    # Since Woodall numbers grow very quickly (W_n = n * 2^n - 1),
    # we only need to check a small range of n values.
    # For n = 10, W_10 = 10 * 1024 - 1 = 10239.
    # For n = 15, W_15 = 15 * 2^15 - 1 = 491519.
    # We can iterate until n * 2^n - 1 exceeds the input number.

    # The input n can be large, but the index k in k * 2^k - 1 
    # will be relatively small (logarithmic/linear-ish).
    k = 1
    while True:
        woodall = k * (2**k) - 1
        if woodall == n:
            return True
        if woodall > n:
            return False
        k += 1

if __name__ == "__main__":
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False