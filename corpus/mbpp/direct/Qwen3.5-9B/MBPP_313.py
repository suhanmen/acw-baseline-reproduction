def pos_nos(numbers):
    return tuple(x for x in numbers if x > 0)

if __name__ == "__main__":
    assert pos_nos([-1, -2, 1, 2]) == (1, 2)
    assert pos_nos([3, 4, -5]) == (3, 4)
    assert pos_nos([-2, -3, 1]) == (1)
    print("All assertions passed.")