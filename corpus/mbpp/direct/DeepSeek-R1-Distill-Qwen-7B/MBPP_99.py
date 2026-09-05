def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = []
    while n > 0:
        remainder = n % 2
        binary.append(str(remainder))
        n = n // 2
    return ''.join(reversed(binary))