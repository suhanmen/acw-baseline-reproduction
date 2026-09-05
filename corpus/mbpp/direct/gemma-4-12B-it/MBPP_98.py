def multiply_num(nums):
    if not nums:
        return 0.0

    product = 1
    for n in nums:
        product *= n

    return float(product / len(nums))

if __name__ == "__main__":
    assert multiply_num((8, 2, 3, -1, 7)) == -67.2
    assert multiply_num((-10, -20, -30)) == -2000.0
    assert multiply_num((19, 15, 18)) == 1710.0