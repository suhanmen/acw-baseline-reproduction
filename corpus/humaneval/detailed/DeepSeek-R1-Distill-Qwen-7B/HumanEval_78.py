def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    """
    if not num:
        return 0

    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0

    for c in num:
        # Convert character to uppercase to handle lowercase inputs
        c_upper = c.upper()
        # Check if the character is a valid hexadecimal digit
        if c_upper in prime_hex_digits:
            count += 1

    return count