def larg_nnum(data, n):
    # Input validation
    if not data or not isinstance(data, list) or len(data) == 0:
        return []
    if not isinstance(n, int) or n < 1:
        return []
    if n > len(data):
        return []

    # Sorting the data in descending order
    sorted_data = sorted(data, reverse=True)

    # Selecting the first 'n' elements
    result = sorted_data[:n]

    # Handling edge cases where all elements in 'result' are equal
    if all(x == result[0] for x in result):
        return [result[0]] * n

    return result