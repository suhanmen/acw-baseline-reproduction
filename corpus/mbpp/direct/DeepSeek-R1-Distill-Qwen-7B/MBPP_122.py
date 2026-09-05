def smartNumber(n):
    def is_smart(num):
        s = str(num)
        for c in s:
            if c not in {'1', '3'}:
                return False
        return True

    count = 0
    num = 1
    while True:
        if is_smart(num):
            count += 1
            if count == n:
                return num
        num += 1