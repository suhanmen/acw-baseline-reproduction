def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start = min(a, b)
    end = max(a, b)

    result = []
    for num in range(start, end + 1):
        # Convert number to string to check if it's a single digit
        s_num = str(num)
        if len(s_num) == 1:
            digit = int(s_num)
            if digit % 2 == 0:
                result.append(digit)

    return sorted(list(set(result)))