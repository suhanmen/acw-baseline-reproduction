def div_even_odd(lst):
    """
    Finds the division of the first even number and the first odd number 
    found in a given list.

    Logic:
    1. Identify the first even number.
    2. Identify the first odd number.
    3. Return the result of first_even / first_odd.
    """
    first_even = None
    first_odd = None

    for num in lst:
        if first_even is None and num % 2 == 0:
            first_even = num
        elif first_odd is None and num % 2 != 0:
            first_odd = num

        # If both are found, we can break early
        if first_even is not None and first_odd is not None:
            break

    if first_even is not None and first_odd is not None:
        return int(first_even / first_odd)
    return None

if __name__ == "__main__":
    assert div_even_odd([1,3,5,7,4,1,6,8]) == 4
    assert div_even_odd([1,2,3,4,5,6,7,8,9,10]) == 2
    assert div_even_odd([1,5,7,9,10]) == 10