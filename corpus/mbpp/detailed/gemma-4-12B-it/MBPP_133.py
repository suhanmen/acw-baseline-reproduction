from typing import List

def sum_negativenum(numbers: List[int]) -> int:
    """
    Calculates the sum of all negative numbers in a list using a lambda function.

    Args:
        numbers (List[int]): A list of integers which may contain positive, 
                              negative, and zero values.

    Returns:
        int: The sum of all negative numbers in the list. Returns 0 if 
             no negative numbers exist or if the list is empty.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # --- Input Validation ---
    # Ensure the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list of integers, got {type(numbers).__name__}")

    # Ensure all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers, found {type(item).__name__}")

    # --- Logic Implementation ---

    # Handle the edge case of an empty list immediately
    if not numbers:
        return 0

    # Define a lambda function to identify if a number is negative.
    # It returns True if the number is strictly less than zero.
    is_negative = lambda x: x < 0

    # Define a lambda function to filter the list.
    # We use the filter function which applies the predicate to every element.
    filter_negatives = lambda lst: list(filter(is_negative, lst))

    # Define a lambda function to perform the summation.
    # The built-in sum() function is passed as the operation.
    calculate_sum = lambda lst: sum(lst)

    # Step 1: Extract only the negative numbers from the source list.
    # This handles cases with mixed signs, only positives, or only negatives.
    negative_numbers_list = filter_negatives(numbers)

    # Step 2: Calculate the total sum of the extracted negative numbers.
    # If the filtered list is empty (no negatives found), sum() returns 0.
    total_sum = calculate_sum(negative_numbers_list)

    return total_sum

# The following assertions verify the logic against the provided test cases.
if __name__ == "__main__":
    # Assertion 1
    assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32

    # Assertion 2
    assert sum_negativenum([10, 15, -14, 13, -18, 12, -20]) == -52

    # Assertion 3
    assert sum_negativenum([19, -65, 57, 39, 152, -639, 121, 44, 90, -190]) == -894

    # Additional edge case checks (not required by prompt but good for production-grade code)
    assert sum_negativenum([]) == 0                # Empty list
    assert sum_negativenum([1, 2, 3]) == 0         # No negatives
    assert sum_negativenum([-1, -2, -3]) == -6     # All negatives
    assert sum_negativenum([0, -1, 1]) == -1       # Inclusion of zero