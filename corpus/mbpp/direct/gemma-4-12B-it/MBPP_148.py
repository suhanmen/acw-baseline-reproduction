def sum_digits_twoparts(n: int) -> int:
    max_sum = 0
    for a in range(n + 1):
        b = n - a
        s_a = sum(int(d) for d in str(a))
        s_b = sum(int(d) for d in str(b))
        if s_a + s_b > max_sum:
            max_sum = s_a + s_b
    return max_sum