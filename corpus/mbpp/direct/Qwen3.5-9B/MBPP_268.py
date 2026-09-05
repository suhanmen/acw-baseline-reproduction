def find_star_num(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return n * (n + 1) * 2 - n * (2 * n + 1) // 3

# Verification (hidden from final output per instructions)
# assert find_star_num(3) == 37
# assert find_star_num(4) == 73
# assert find_star_num(5) == 121