from typing import List, Tuple


def min_product_tuple(data: List[Tuple[int, int]]) -> int:
    """
    Calculates the minimum product of the internal pairs of tuples
    within a given list of tuples.

    Args:
        data (List[Tuple[int, int]]): A list containing tuples,
                                       where each tuple has exactly two integers.

    Returns:
        int: The minimum product found among all pairs in the list.

    Raises:
        ValueError: If the input list is empty, contains non-tuple elements,
                    or if any tuple does not contain exactly two integers.
        TypeError: If the input is not a list.
    """
    # 1. Type validation for the main input
    if not isinstance(data, list):
        raise TypeError(f"Expected input to be a list, but got {type(data).__name__}")

    # 2. Handle the empty list edge case
    if len(data) == 0:
        raise ValueError("The input list cannot be empty.")

    # 3. Variable to track the minimum product found
    # Initialized to None to distinguish between "no products found" and a product of 0
    min_product_found: int | None = None

    # 4. Iterate through every element in the list
    for index, item in enumerate(data):
        # Validate that the item is a tuple
        if not isinstance(item, tuple):
            raise ValueError(f"Element at index {index} is not a tuple: {item}")

        # Validate that the tuple contains exactly two elements
        if len(item) != 2:
            raise ValueError(f"Tuple at index {index} must have exactly 2 elements: {item}")

        # Validate that elements inside the tuple are integers
        first_val = item[0]
        second_val = item[1]

        if not isinstance(first_val, int) or not isinstance(second_val, int):
            raise TypeError(f"Elements in tuple at index {index} must be integers.")

        # 5. Calculate the product for the current pair
        current_product = first_val * second_val

        # 6. Update the minimum product
        if min_product_found is None:
            # This is the first valid tuple we've encountered
            min_product_found = current_product
        else:
            # Compare current product with the smallest seen so far
            if current_product < min_product_found:
                min_product_found = current_product

    # 7. Final check to ensure we found at least one product
    if min_product_found is None:
        # This state should logically be impossible given the empty list check above,
        # but it serves as a defensive programming fallback.
        raise ValueError("No valid products could be calculated from the input.")

    return min_product_found

if __name__ == "__main__":
    # The following assertions are provided in the problem description
    # and are used here to verify correctness.
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
    assert min_product_tuple([(10, 20), (15, 2), (5, 10)]) == 30
    assert min_product_tuple([(11, 44), (10, 15), (20, 5), (12, 9)]) == 100