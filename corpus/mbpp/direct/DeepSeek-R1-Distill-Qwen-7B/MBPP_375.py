def round_num(n, multiple):
    return int((n + multiple // 2) // multiple) * multiple

assert round_num(4722,10)==4720
assert round_num(1111,5)==1110
assert round_num(219,2)==218