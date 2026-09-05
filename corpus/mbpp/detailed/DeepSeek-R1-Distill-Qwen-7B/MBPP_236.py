def No_of_Triangle(n, k):
    # Check if inputs are valid
    if not isinstance(n, int) or not isinstance(k, int):
        return -1
    if n < 1 or k < 1:
        return -1
    if k == 0:
        return 0
    # Calculate the maximum number of equilateral triangles
    total = 0
    for row in range(1, k + 1):
        total += row * (row + 1) // 2
    return total