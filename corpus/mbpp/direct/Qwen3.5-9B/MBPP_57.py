def find_Max_Num(digits, n):
    if n != len(digits):
        raise ValueError("The length of digits must match n.")
    digits.sort(reverse=True)
    return int("".join(map(str, digits)))