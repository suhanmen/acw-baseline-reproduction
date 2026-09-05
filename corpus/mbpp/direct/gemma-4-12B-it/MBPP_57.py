def find_Max_Num(digits, n):
    """
    Finds the largest number that can be formed using the first n digits
    from the provided list.
    """
    # Sort the digits in descending order to form the largest number
    sorted_digits = sorted(digits[:n], reverse=True)

    # Join the sorted digits into a single integer
    result = int("".join(map(str, sorted_digits)))

    return result