def round_and_sum(numbers):
    # Step 1: Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")

    # Check if all elements are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")

    # Step 2: Handle empty list
    if not numbers:
        print(0)
        return

    # Step 3: Round each number and calculate the sum
    rounded = [round(num) for num in numbers]
    total = sum(rounded)

    # Step 4: Multiply by the length of the list
    result = total * len(numbers)

    # Step 5: Print the result
    print(result)