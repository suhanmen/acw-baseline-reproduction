def find_Parity(number):
    """
    Determines the parity of a given integer.
    Returns "Even Parity" if the number is even, and "Odd Parity" if odd.
    """
    if number % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"