import typing

def bell_number(n: int) -> int:
    """
    Calculates the n-th Bell number.

    The Bell number B_n counts the number of ways to partition a set of n 
    elements into non-empty subsets.

    The values are generated using the Bell Triangle (also known as Aitken's 
    array or the Peirce triangle).

    Args:
        n (int): The index of the Bell number to calculate (n >= 0).

    Returns:
        int: The n-th Bell number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    # --- Input Validation ---
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer. Received: {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input 'n' must be a non-negative integer. Received: {n}")

    # --- Edge Case Handling ---
    # B_0 is defined as 1 (the empty set has one partition: itself)
    if n == 0:
        return 1

    # B_1 is 1
    if n == 1:
        return 1

    # --- Algorithm Implementation ---
    # We use the Bell Triangle method to calculate the values.
    # The triangle is constructed such that:
    # 1. The first row is [1].
    # 2. For each subsequent row, the first element is the last element of the previous row.
    # 3. Each subsequent element in a row is the sum of the element to its left 
    #    and the element directly above that left neighbor.
    #
    # Example for n=3:
    # Row 0: 1
    # Row 1: 1, 2
    # Row 2: 2, 3, 5
    # Row 3: 5, 7, 10, 15
    # The Bell numbers are the first (or last) elements of each row.

    # We only need to store the current row to compute the next one,
    # or we can build the triangle row by row. 
    # To be memory efficient while maintaining clarity, we will store rows.

    # triangle[i] will hold the i-th row of the Bell triangle.
    # We initialize it with the first row.
    bell_triangle: typing.List[typing.List[int]] = []
    bell_triangle.append([1])

    # Iterate from 1 up to n (inclusive)
    # Note: bell_triangle[0] corresponds to n=0.
    # We need to reach the row that contains the result for n.
    for i in range(1, n + 1):
        # Get the previous row to construct the current row
        previous_row = bell_triangle[i - 1]
        current_row_length = i + 1
        current_row = [0] * current_row_length

        # Rule 1: The first element of the current row is 
        # the last element of the previous row.
        last_val_prev_row = previous_row[-1]
        current_row[0] = last_val_prev_row

        # Rule 2: Fill the rest of the row.
        # current_row[j] = current_row[j-1] + previous_row[j-1]
        for j in range(1, current_row_length):
            left_neighbor = current_row[j - 1]
            above_left_neighbor = previous_row[j - 1]
            current_row[j] = left_neighbor + above_left_neighbor

        bell_triangle.append(current_row)

    # The n-th Bell number is the first element of the n-th row 
    # in the standard construction (where index 0 is B_0).
    # However, based on the triangle logic:
    # Row 0: [1] -> B_0 = 1
    # Row 1: [1, 2] -> B_1 = 1 (The first element of Row 1 is B_0, 
    # but the triangle logic actually makes the first element of row i 
    # equal to B_{i-1} and the last element equal to B_i).

    # Let's trace:
    # Row 0: [1] -> B_0 = 1
    # Row 1: [1, 2] -> B_1 is the first element of Row 1? No, B_1=1.
    # Actually, the standard definition is that B_n is the first element 
    # of row n, but the row index starts at 0.
    # Let's re-verify:
    # n=0: row [1] -> B_0 = 1
    # n=1: row [1, 2] -> B_1 = 1 (Wait, B_1 is 1. The first element of row 1 is 1.)
    # n=2: row [2, 3, 5] -> B_2 = 2.
    # Therefore, B_n is the first element of the n-th row of the triangle 
    # where the triangle is built such that the first element of row i is B_{i-1}.
    # This means we need to look at the first element of the n-th row.

    # To match the assertions:
    # bell_number(2) == 2
    # Row 0: [1]
    # Row 1: [1, 2]
    # Row 2: [2, 3, 5]
    # Indexing:
    # bell_triangle[0][0] is B_0 = 1
    # bell_triangle[1][0] is B_1 = 1
    # bell_triangle[2][0] is B_2 = 2
    # bell_triangle[3][0] is B_3 = 5

    # Let's check bell_number(10).
    # My logic: The first element of bell_triangle[n] is B_n.
    # Let's double check the triangle construction:
    # Row 0: B0
    # Row 1: B0, B0+B0=B1? No.
    # Construction:
    # Row 0: 1
    # Row 1: 1, 2
    # Row 2: 2, 3, 5
    # Row 3: 5, 7, 10, 15
    # Here, B0=1, B1=1, B2=2, B3=5, B4=15.
    # The first element of row n is B_n.
    # Wait, if row 1 is [1, 2], the first element is 1.
    # If row 2 is [2, 3, 5], the first element is 2.
    # If row 3 is [5, 7, 10, 15], the first element is 5.
    # This matches the property B_n = first element of row n.

    # Wait, let's re-calculate for n=1. 
    # If n=1, loop runs for i=1.
    # previous_row = [1]
    # current_row = [1, 2]
    # bell_triangle = [[1], [1, 2]]
    # return bell_triangle[1][0] -> 1. Correct.

    # Let's re-calculate for n=2.
    # i=1: current_row = [1, 2]
    # i=2: previous_row = [1, 2], current_row = [2, 3, 5]
    # return bell_triangle[2][0] -> 2. Correct.

    return bell_triangle[n][0]