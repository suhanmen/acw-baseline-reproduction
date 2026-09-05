def dig_let(s: str) -> tuple:
    letters = 0
    digits = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return (letters, digits)

if __name__ == "__main__":
    assert dig_let("python") == (6, 0)
    assert dig_let("program") == (7, 0)
    assert dig_let("python3.0") == (6, 2)