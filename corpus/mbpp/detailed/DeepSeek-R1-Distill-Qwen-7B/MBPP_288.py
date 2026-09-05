def modular_inverse(arr, p, prime):
    count = 0
    for a in arr:
        if a % prime == 0:
            continue  # Skip elements that are multiples of p (not coprime)
        if (a * a) % prime == 1:
            count += 1
    return count