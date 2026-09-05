from typing import List


def sum_three_smallest_nums(numbers: List[int]) -> int:
    """
    Finds the sum of the three lowest positive numbers from a given list of numbers.

    Positive numbers are defined as numbers strictly greater than zero (> 0).
    If there are fewer than three positive numbers, the sum of all available 
    positive numbers is returned.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The sum of the three smallest positive numbers.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input Validation: Check if the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Input Validation: Check if all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Step 1: Filter out numbers that are not positive (<= 0)
    # We only care about numbers strictly greater than 0.
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)

    # Step 2: Handle the case where there are no positive numbers
    if not positive_numbers:
        return 0

    # Step 3: Sort the positive numbers in ascending order
    # We create a copy to avoid mutating the original list (defensive programming)
    sorted_positives = sorted(positive_numbers)

    # Step 4: Determine how many numbers to sum
    # If there are fewer than 3, we take all of them.
    # Otherwise, we take exactly the first 3.
    count_to_take = 3
    available_count = len(sorted_positives)

    if available_count < count_to_take:
        count_to_take = available_count

    # Step 5: Extract the subset of the smallest numbers
    smallest_three = sorted_positives[:count_to_take]

    # Step 6: Calculate and return the sum
    total_sum = 0
    for value in smallest_three:
        total_sum += value

    return total_sum