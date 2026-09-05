def newman_prime(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    newman_shanks_williams = [1, 2, 3, 5, 7, 17, 31, 41, 73, 121, 233, 589, 733, 853, 1123, ...]

    def generate_nsws(limit):
        a, b = 1, 1
        j = 1
        idx = 0
        seq = set()
        while len(seq) < limit and j <= limit:
            a, b = b, a + b
            j *= 2
            x = (b - a) // 2
            if x in seq:
                continue
            is_prime = True
            if x < 2:
                is_prime = False
            else:
                for k in range(2, int(x**0.5) + 1):
                    if x % k == 0:
                        is_prime = False
                        break
            if is_prime:
                seq.add(x)
                idx += 1
                if idx == limit:
                    yield x
            j //= 2
            a, b = b, a + b
            j *= 2
        yield 1 if not seq else (next(seq) if seq else 1)

    def newman_shanks_williams_sequence(n):
        if n == 1:
            yield 1
            return
        a, b = 1, 1
        j = 1
        idx = 1
        seq = set()
        while len(seq) < n:
            a, b = b, a + b
            j *= 2
            x = (b - a) // 2
            if x in seq or x <= 0:
                continue
            is_prime = True
            for k in range(2, int(x**0.5) + 1):
                if x % k == 0:
                    is_prime = False
                    break
            if is_prime:
                seq.add(x)
                idx += 1
                if idx == n:
                    return
        yield from seq

    count = 0
    value = 1
    for p in newman_shanks_williams_sequence(n):
        if p == value:
            continue
        value = p
        count += 1
        if count == n:
            return value
    return 1