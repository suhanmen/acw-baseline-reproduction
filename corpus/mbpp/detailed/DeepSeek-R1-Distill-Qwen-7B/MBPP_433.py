def check_greater(numbers, entered_number):
    # Check if the array is empty
    if not numbers:
        return "No, entered number is less than those in the array"

    # Flag to track if any element is greater than or equal to the entered number
    has_greater_or_equal = False

    # Iterate through each number in the array
    for num in numbers:
        if num >= entered_number:
            has_greater_or_equal = True
            break  # No need to check further

    # If any element is greater or equal, return 'No'
    if has_greater_or_equal:
        return "No, entered number is less than those in the array"
    else:
        return "Yes, the entered number is greater than those in the array"