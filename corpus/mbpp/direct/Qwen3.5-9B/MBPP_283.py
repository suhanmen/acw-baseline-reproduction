def validate(n: int) -> bool:
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    digits = str(n)
    freq = {}

    for d in digits:
        d = int(d)
        freq[d] = freq.get(d, 0) + 1

    for d, count in freq.items():
        if count > d:
            return False
    return True