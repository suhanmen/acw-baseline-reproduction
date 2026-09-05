def multiple_to_single(lst):
    if not lst:
        return 0
    sign = 1
    if any(num < 0 for num in lst):
        sign = -1
    abs_numbers = [str(abs(num)) for num in lst]
    concatenated = ''.join(abs_numbers)
    return sign * int(concatenated)