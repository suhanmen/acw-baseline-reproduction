def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    # Handle the case where num is 0 immediately
    if num == 0:
        return (1, 0)

    # Convert the number to its absolute value string to handle negatives
    str_num = str(abs(num))
    even_count = 0
    odd_count = 0

    for ch in str_num:
        digit = int(ch)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)