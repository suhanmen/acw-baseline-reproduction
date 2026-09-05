def first_Factorial_Divisible_Number(x):
    n = 1
    current_fact = 1
    while True:
        if current_fact % x == 0:
            return n
        n += 1
        current_fact *= n