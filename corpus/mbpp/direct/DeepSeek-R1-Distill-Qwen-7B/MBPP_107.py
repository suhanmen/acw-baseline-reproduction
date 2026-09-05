def count_Hexadecimal(a, b):
    count = 0
    for num in range(a, b + 1):
        hex_num = format(num, 'x')
        if len(hex_num) % 2 == 0:
            count += 1
    return count