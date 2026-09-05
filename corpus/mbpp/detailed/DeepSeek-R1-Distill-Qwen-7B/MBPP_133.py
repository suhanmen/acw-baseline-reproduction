def sum_negative_numbers(numbers):
    """
    Calculate the sum of the negative numbers in a given list.

    Args:
        numbers: A list of numbers to be processed.

    Returns:
        The sum of all negative numbers in the list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not a number.
    """
    # Validate the input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    # Check if all elements are numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers.")

    # Filter out negative numbers and sum them
    negatives = [num for num in numbers if num < 0]

    # Sum the negatives
    sum_neg = sum(negatives)

    # Return the sum of negatives
    return sum_neg

# Example usage and assertions
def sum_negativenum(lst):
    return sum_negative_numbers(lst)

assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
assert sum_negativenum([10, 15, -14, 13, -18, 12, -20]) == -52
assert sum_negativenum([19, -65, 57, 39, 152, -639, 121, 44, 90, -190]) == -894