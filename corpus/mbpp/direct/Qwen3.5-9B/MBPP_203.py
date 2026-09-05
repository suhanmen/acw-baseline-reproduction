def hamming_Distance(n1, n2):
    xor = n1 ^ n2
    distance = 0
    while xor:
        if xor & 1:
            distance += 1
        xor >>= 1
    return distance