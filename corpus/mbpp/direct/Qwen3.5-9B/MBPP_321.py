def find_demlo(n_str: str) -> str:
    n = len(n_str)
    if n == 0:
        return ""

    # Generate the sequence 1, 2, ..., n as strings
    seq = [str(i + 1) for i in range(n)]

    # Reverse the first part up to the middle
    mid = n // 2
    first_part = seq[:mid][::-1]

    # The second part is the reverse of the first part excluding the middle element if n is odd
    if n % 2 == 1:
        second_part = first_part[:-1][::-1]
    else:
        second_part = first_part[::-1]

    return "".join(first_part) + "".join(second_part)