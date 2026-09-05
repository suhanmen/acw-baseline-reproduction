def sequence(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    seq = [0] * (n + 1)
    seq[1] = 1
    seq[2] = 1

    for i in range(3, n + 1):
        seq[i] = seq[seq[i-2]] + seq[i-1]

    return seq[n]