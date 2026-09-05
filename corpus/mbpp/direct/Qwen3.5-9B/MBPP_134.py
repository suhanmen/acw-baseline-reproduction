def check_last(arr, p, operation):
    if operation == 1:
        last = arr[-1]
        for _ in range(p):
            if last % 2 == 0:
                last += 1
            else:
                last += 2
    else:
        last = arr[-1]
        for _ in range(p):
            if last % 2 == 0:
                last += 2
            else:
                last += 1

    return "EVEN" if last % 2 == 0 else "ODD"