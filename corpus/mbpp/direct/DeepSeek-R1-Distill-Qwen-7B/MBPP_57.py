def find_Max_Num(digits):
    # Sort the digits in descending order to get the largest possible number
    sorted_digits = sorted(digits, reverse=True)
    # Join the sorted digits into a string and convert it to an integer
    return int(''.join(map(str, sorted_digits)))