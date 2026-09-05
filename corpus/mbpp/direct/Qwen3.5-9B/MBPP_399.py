def bitwise_xor(tuple1: tuple, tuple2: tuple) -> tuple:
    return tuple(a ^ b for a, b in zip(tuple1, tuple2))