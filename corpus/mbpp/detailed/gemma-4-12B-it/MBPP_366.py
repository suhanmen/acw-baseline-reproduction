from typing import List


def adjacent_num_product(numbers: List[int]) -> int:
    """
    Calculates the largest product of any two adjacent elements in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The largest product found between adjacent elements.

    Raises:
        ValueError: If the input list has fewer than two elements.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, received {type(numbers).__name__}")

    # Validate the size of the list
    list_length = len(numbers)
    if list_length < 2:
        raise ValueError("Input list must contain at least two elements to form an adjacent pair.")

    # Validate that all elements are integers
    for index, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(f"Element at index {index} is {type(element).__name__}, expected int.")

    # Initialize the maximum product. 
    # Using the product of the first two elements ensures we handle negative numbers correctly,
    # as the max product could be negative if all adjacent products are negative.
    first_element = numbers[0]
    second_element = numbers[1]
    max_product = first_element * second_element

    # Iterate through the list to find all adjacent pairs
    # We stop at list_length - 1 to ensure i + 1 is within bounds.
    for i in range(list_length - 1):
        current_left = numbers[i]
        current_right = numbers[i + 1]

        # Calculate product of the current pair
        current_product = current_left * current_right

        # Update max_product if the current one is larger
        if current_product > max_product:
            max_product = current_product

    return max_product

if __name__ == "__main__":
    # Test cases provided in the prompt
    assert adjacent_num_product([1, 2, 3, 4, 5, 6]) == 30
    assert adjacent_num_product([1, 2, 3, 4, 5]) == 20
    assert adjacent_num_product([2, 3]) == 6

    # Additional edge cases
    assert adjacent_num_product([-1, -2, -3]) == 6      # Negative products ((-1)*(-2)=2, (-2)*(-3)=6)
    assert adjacent_num_product([-5, 2, -10]) == -10      # All products negative or mixed
    assert adjacent_num_product([0, 5, 0]) == 0            # Zeros
    assert adjacent_num_product([10, 10, 10]) == 100       # All equal