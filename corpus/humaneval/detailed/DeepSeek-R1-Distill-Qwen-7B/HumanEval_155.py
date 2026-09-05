def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Handle the case where the number is 0 immediately
    if num == 0:
        return (1, 0)

    # Convert the number to its absolute value to handle negatives
    number = abs(num)
    digits = str(number)
    even_count = 0
    odd_count = 0

    for digit in digits:
        # Convert each character back to integer
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)