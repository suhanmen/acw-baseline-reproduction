from typing import List

def count_odd(numbers: List[int]) -> int:
    """
    Finds the number of odd elements in a given list of integers 
    using a lambda function.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The count of odd integers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected input type 'list', but received '{type(numbers).__name__}'.")

    # Handle the edge case of an empty list explicitly
    if len(numbers) == 0:
        return 0

    # Validate that all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Define a lambda function to check if a number is odd.
    # A number is odd if its remainder when divided by 2 is non-zero.
    # This correctly handles positive and negative integers.
    is_odd = lambda x: x % 2 != 0

    # Filter the list to keep only the odd numbers.
    # We use the filter function which applies the lambda to each element.
    odd_elements_iterator = filter(is_odd, numbers)

    # Convert the filter result into a list to count the elements.
    odd_elements_list = list(odd_elements_iterator)

    # Calculate the final count
    count = len(odd_elements_list)

    return count

# Assertion tests to ensure correctness
if __name__ == "__main__":
    # Test case 1: Mix of positive odd and even
    assert count_odd([1, 2, 3, 5, 7, 8, 10]) == 4

    # Test case 2: Mix of positive, negative, and odd/even
    # -18 is even, -20 is even, 15 and 13 are odd
    assert count_odd([10, 15, 14, 13, -18, 12, -20]) == 2

    # Test case 3: Sparse odd numbers
    assert count_odd([1, 2, 4, 8, 9]) == 2

    # Additional edge cases
    assert count_odd([]) == 0 # Empty list
    assert count_odd([2, 4, 6]) == 0 # No odd numbers
    assert count_odd([1, 3, 5]) == 3 # All odd numbers
    assert count_odd([0]) == 0 # Zero is even
    assert count_odd([-1, -3, -5]) == 3 # All negative odd