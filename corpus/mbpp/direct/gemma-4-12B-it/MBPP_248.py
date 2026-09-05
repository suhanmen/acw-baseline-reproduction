def harmonic_sum(n):
    """
    Calculates the harmonic sum of n-1.
    The harmonic sum H_k is defined as the sum of 1/i for i from 1 to k.
    In this context, the problem asks for the sum of 1/i for i from 1 to n-1.
    """
    harmonic_sum_val = 0.0
    for i in range(1, n):
        harmonic_sum_val += 1.0 / i
    return harmonic_sum_val

if __name__ == "__main__":
    assert harmonic_sum(7) == 2.5928571428571425
    assert harmonic_sum(4) == 2.083333333333333
    assert harmonic_sum(19) == 3.547739657143682