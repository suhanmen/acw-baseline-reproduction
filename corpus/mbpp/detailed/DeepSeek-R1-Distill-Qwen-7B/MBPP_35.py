def find_rect_num(n):
    # Validate the input
    if not isinstance(n, int):
        return "Invalid input: n must be an integer"
    if n < 1:
        return "Invalid input: n must be a positive integer"

    # Calculate the n-th rectangular number
    return n * (n + 1)

# Test cases
print(find_rect_num(4))  # Output: 20
print(find_rect_num(5))  # Output: 30
print(find_rect_num(6))  # Output: 42