def No_of_Triangle(side: int, small_side: int) -> int:
    if small_side > side:
        return -1
    if small_side == 0:
        return 0
    if side == 1:
        return 1 if small_side == 1 else 0
    n = side - small_side + 1
    total = n * n - (n - 1) * (n - 1) + (n - 1) * (n - 2) // 2
    return total if total > 0 else 0

if __name__ == "__main__":
    assert No_of_Triangle(4, 2) == 7
    assert No_of_Triangle(4, 3) == 3
    assert No_of_Triangle(1, 3) == -1