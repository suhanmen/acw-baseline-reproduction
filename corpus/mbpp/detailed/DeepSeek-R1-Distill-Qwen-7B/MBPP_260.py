def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_ns_sequence(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            s = [1, 2]
            for i in range(2, n + 1):
                next_s = 2 * s[i-1] + s[i-2]
                s.append(next_s)
            return s

    sequence = generate_ns_sequence(n)
    for num in sequence:
        if is_prime(num):
            return num
    return None  # This line is theoretically unreachable if n is valid

# Test cases
assert newman_prime(3) == 7 
assert newman_prime(4) == 17
assert newman_prime(5) == 41