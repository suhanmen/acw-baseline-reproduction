def compute_Last_Digit(a: int, b: int) -> int:
    if a > b:
        return -1  # Undefined case for a > b

    if b < 10:
        b_fact = 1
        for i in range(2, b + 1):
            b_fact *= i
        if a < b_fact:
            # Direct division for small factorials
            if b_fact % a == 0:
                return b_fact // a
            else:
                return -1
    else:
        # For b >= 10, b! always has last digit 0 and is divisible by any a <= b
        # unless a is 0 (but factorial is defined for positive integers here)
        return 0

    # This line should technically not be reached if logic above covers all cases
    return -1