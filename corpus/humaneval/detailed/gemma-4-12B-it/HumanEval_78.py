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
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """

    # Define the target prime digits in hexadecimal.
    # 2 is prime.
    # 3 is prime.
    # 5 is prime.
    # 7 is prime.
    # B is 11 in decimal, which is prime.
    # D is 13 in decimal, which is prime.
    # Other hex digits (0, 1, 4, 6, 8, 9, A(10), C(12), E(14), F(15)) are not prime.
    PRIME_HEX_DIGITS = {'2', '3', '5', '7', 'B', 'D'}

    # Initialize a counter to keep track of prime digits found.
    prime_count = 0

    # Handle the case where the input might be None, though the prompt 
    # says it will be a string or empty string.
    if num is None:
        return 0

    # Ensure the input is treated as a string.
    input_string = str(num)

    # Iterate through each character in the input string.
    for character in input_string:
        # Check if the current character is one of our identified prime digits.
        # This handles both numeric characters and uppercase letters as specified.
        is_prime_digit = character in PRIME_HEX_DIGITS

        if is_prime_digit:
            # Increment the counter if the character matches.
            prime_count += 1

    # Return the final count of prime hexadecimal digits.
    return prime_count