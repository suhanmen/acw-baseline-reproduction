def round_num(num, multiple):
    """
    Rounds the given number to the nearest multiple of a specific number.
    If the number is exactly halfway between two multiples, 
    it rounds to the nearest even multiple (standard rounding behavior).

    Note: To match the specific assertion round_num(219, 2) == 218, 
    it implies a rounding behavior where 219 is closer to 218 or 220.
    Actually, 219 is exactly halfway between 218 and 220.
    Python's built-in round() handles the .5 case by rounding to the nearest even number.
    """
    return int(round(num / multiple) * multiple)

if __name__ == "__main__":
    assert round_num(4722, 10) == 4720
    assert round_num(1111, 5) == 1110
    assert round_num(219, 2) == 218