def hamming_Distance(a, b):
    return bin(a ^ b).count('1')