def bell_number(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    # Bell numbers can be computed using the Bell triangle (Aitken's array)
    # Triangle construction:
    # Row 1: [1]
    # Row 2: [2, 3]
    # Row 3: [5, 7, 10]
    # Row 4: [15, 20, 27, 37]
    # ...
    # The last element of row i (0-indexed) is Bell(i)

    if n == 0:
        return 1

    bell = [0] * (n + 1)
    bell[0] = 1

    current_row = [0]
    current_row[0] = 1

    for i in range(1, n + 1):
        next_row = []
        # First element of new row is last element of previous row
        next_row.append(current_row[-1])

        # Build the rest of the row
        for j in range(len(current_row)):
            prev_val = current_row[j]
            new_val = current_row[j] + next_row[-1] if j > 0 else current_row[0] + next_row[-1]
            # Actually, correct logic:
            # For row i (length i), elements are:
            # first = last of previous row
            # subsequent = previous_row[j] + current_row[j-1] (but we build sequentially)
            pass

        # Let's rebuild with correct Bell triangle logic
        # Row 0: [1]
        # Row 1: [1+1=2, ...] -> Actually standard triangle:
        # Start with T[0][0] = 1
        # T[i][0] = T[i-1][i-1] (last element of previous row)
        # T[i][j] = T[i][j-1] + T[i-1][j-1] for j > 0

        if i == 1:
            current_row = [1]
        else:
            new_row = [current_row[-1]]  # First element
            for j in range(1, i + 1):
                # T[i][j] = T[i][j-1] + T[i-1][j-1]
                # current_row represents row i-1
                # new_row[j-1] is T[i][j-1]
                # current_row[j-1] is T[i-1][j-1] (but current_row has length i)
                val = new_row[-1] + current_row[j-1]
                new_row.append(val)
            current_row = new_row

        bell[i] = current_row[-1]

    return bell[n]