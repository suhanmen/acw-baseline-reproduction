from typing import List, Tuple, Union


def validate_numbers(numbers: List[Union[int, float]]) -> None:
    """
    Validates that the input list contains only integers and is not None.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    if numbers is None:
        raise TypeError("Input must be a list of integers.")

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    for index, value in enumerate(numbers):
        if not isinstance(value, int):
            # Note: bool is a subclass of int in Python, but typically we want strict ints.
            # However, the type hint says List[int], so we should arguably reject booleans
            # if they were passed explicitly (e.g., [1, True]), though technically True==1.
            # For strict production safety against common pitfalls, we reject booleans.
            if isinstance(value, bool):
                raise TypeError(f"Boolean values are not allowed as integers. Found at index {index}.")
            raise TypeError(f"All elements must be integers. Found non-integer at index {index}: {value!r} (type: {type(value).__name__}).")


def compute_sum(numbers: List[int]) -> int:
    """
    Computes the sum of all integers in the list.
    Uses an explicit loop for clarity and debugging capability.
    """
    total_sum: int = 0

    for number in numbers:
        current_sum = total_sum + number
        # Update total_sum explicitly
        total_sum = current_sum

    return total_sum


def compute_product(numbers: List[int]) -> int:
    """
    Computes the product of all integers in the list.
    Handles the empty list case explicitly by returning 1.
    """
    if len(numbers) == 0:
        return 1

    total_product: int = 1

    for number in numbers:
        # Explicitly check for zero to potentially optimize or log, though math holds naturally.
        if number == 0:
            total_product = 0
            # We can break here for efficiency, but for explicit step-by-step logic demonstration,
            # we might continue. However, once product is zero, it stays zero.
            # Let's break for efficiency in the explicit step.
            break

        intermediate_product = total_product * number
        total_product = intermediate_product

    return total_product


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple (sum_value, product_value).

    Raises:
        TypeError: If the input is not a list of integers.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
        >>> sum_product([0, 5])
        (5, 0)
        >>> sum_product([-1, -2])
        (-3, 2)
    """
    # Step 1: Validate the input data explicitly
    validate_numbers(numbers)

    # Step 2: Calculate the sum using the helper function
    calculated_sum = compute_sum(numbers)

    # Step 3: Calculate the product using the helper function
    calculated_product = compute_product(numbers)

    # Step 4: Return the result as a tuple
    return (calculated_sum, calculated_product)