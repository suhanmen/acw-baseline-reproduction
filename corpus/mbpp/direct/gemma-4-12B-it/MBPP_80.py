def tetrahedral_number(n: int) -> float:
    """
    Calculates the nth tetrahedral number.
    The formula for the nth tetrahedral number is T_n = (n * (n + 1) * (n + 2)) / 6.
    """
    return (n * (n + 1) * (n + 2)) / 6.0

if __name__ == "__main__":
    assert tetrahedral_number(5) == 35.0
    assert tetrahedral_number(6) == 56.0
    assert tetrahedral_number(7) == 84.0