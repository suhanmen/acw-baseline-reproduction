def find_star_num(n):
    # Validate the input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")

    # Calculate the nth star number
    star_num = 6 * n * (n - 1) + 1

    return star_num