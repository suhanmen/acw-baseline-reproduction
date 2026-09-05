def num_comm_div(a, b):
    if a == 0 or b == 0:
        return 0
    i = 1
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            current_gcd = i
        i += 1
    return current_gcd