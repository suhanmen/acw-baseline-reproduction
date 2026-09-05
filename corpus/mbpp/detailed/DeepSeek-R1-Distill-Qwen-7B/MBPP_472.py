def check_consecutive(numbers):
    # Input validation: Check if the input is a list
    if not isinstance(numbers, list):
        return False

    # Check if all elements are integers
    if not all(isinstance(n, int) for n in numbers):
        return False

    # Handle edge cases
    if len(numbers) == 0:
        return False  # Empty list is not consecutive
    if len(set(numbers)) == 1:
        return False  # All elements are the same; cannot be consecutive

    # Check if the list has at least two elements
    if len(numbers) < 2:
        return True  # A single element is trivially consecutive

    # Convert the list to a sorted list
    sorted_numbers = sorted(numbers)

    # Calculate the expected difference between consecutive numbers
    first_diff = sorted_numbers[1] - sorted_numbers[0]

    # Check if the difference is 1 (consecutive starts here)
    if first_diff != 1:
        return False

    # Ensure all numbers are consecutive by checking the max - min difference
    max_num = sorted_numbers[-1]
    min_num = sorted_numbers[0]
    if max_num - min_num == len(numbers) - 1:
        return True
    else:
        return False