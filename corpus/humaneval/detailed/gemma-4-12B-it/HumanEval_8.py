from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Input Validation: Ensure the input is a list.
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but got {type(numbers).__name__}")

    # Input Validation: Ensure all elements in the list are integers.
    for index, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(
                f"All elements in the list must be integers. "
                f"Found {type(item).__name__} at index {index}."
            )

    # Define the initial identity values.
    # The identity for addition is 0.
    # The identity for multiplication is 1.
    initial_sum: int = 0
    initial_product: int = 1

    # If the list is empty, the result is the identity values.
    if not numbers:
        return (initial_sum, initial_product)

    # Initialize running accumulators.
    current_sum: int = initial_sum
    current_product: int = initial_product

    # Iterate through the numbers to calculate the cumulative sum and product.
    # We process each number explicitly to ensure visibility of the logic.
    for number in numbers:
        # Update the sum.
        current_sum += number

        # Update the product.
        # Note: If any number in the sequence is 0, the product will become 0 
        # and remain 0 for all subsequent elements.
        current_product *= number

    # Package the results into a tuple.
    final_result_sum: int = current_sum
    final_result_product: int = current_product

    return (final_result_sum, final_result_product)