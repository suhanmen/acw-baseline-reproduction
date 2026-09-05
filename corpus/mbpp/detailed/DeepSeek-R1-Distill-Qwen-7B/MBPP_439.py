def multiple_to_single(numbers):
    # Validate input: check if numbers is a list and each element is an integer
    if not isinstance(numbers, list):
        return 0
    for num in numbers:
        if not isinstance(num, int):
            return 0

    # Handle empty list case
    if not numbers:
        return 0

    # Handle single element case
    if len(numbers) == 1:
        return numbers[0]

    # Initialize the concatenated string
    concatenated = ''

    # Convert each number to string and concatenate
    for num in numbers:
        concatenated += str(num)

    # Convert the concatenated string to integer
    return int(concatenated)