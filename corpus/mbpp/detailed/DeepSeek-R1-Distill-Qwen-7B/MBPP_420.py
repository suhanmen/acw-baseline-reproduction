def cube_Sum(n):
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Handle edge cases
    if n == 0:
        return 0

    # Generate the first n even numbers
    even_numbers = [2 * i for i in range(1, n + 1)]

    # Compute the cube of each even number
    cubes = [num ** 3 for num in even_numbers]

    # Calculate the sum of cubes
    cube_sum = sum(cubes)

    return cube_sum

# Example usage:
# cube_Sum(2) should return 72
# cube_Sum(3) should return 288
# cube_Sum(4) should return 800