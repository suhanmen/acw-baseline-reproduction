def find_Average_Of_Cube(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return None

    # Generate the first n natural numbers and compute their cubes
    cubes = [i ** 3 for i in range(1, n + 1)]

    # Sum all the cubes
    sum_of_cubes = sum(cubes)

    # Calculate the average
    average = sum_of_cubes / n

    return average