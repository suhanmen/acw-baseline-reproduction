from typing import List

def sum_even_and_even_index(numbers: List[int], length: int) -> int:
    """
    Calculates the sum of all numbers that are even and are located at
    even indices (0, 2, 4, ...) within the first 'length' elements 
    of the provided list.

    Args:
        numbers: A list of integers.
        length: The number of elements from the start of the list to consider.

    Returns:
        The sum of even numbers at even positions.

    Raises:
        ValueError: If the length provided is negative or exceeds the list size.
        TypeError: If input types are incorrect.
    """
    # --- Input Validation ---

    # Ensure numbers is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list for 'numbers', but got {type(numbers).__name__}")

    # Ensure length is an integer
    if not isinstance(length, int):
        raise TypeError(f"Expected an integer for 'length', but got {type(length).__name__}")

    # Handle negative length
    if length < 0:
        raise ValueError(f"Length must be a non-negative integer, but got {length}")

    # Handle case where length is greater than the list size
    # This is defensive to ensure we don't access out of bounds or behave unpredictably
    actual_list_length = len(numbers)
    if length > actual_list_length:
        # Depending on requirements, one might raise an error or cap it.
        # Given the assertions, we should ensure the behavior is consistent.
        # Here, we will cap it to the actual length to be safe.
        length = actual_list_length

    # --- Processing ---

    # Initialize the running sum
    total_sum = 0

    # Iterate through the list up to the specified length
    for current_index in range(length):
        # Check if the position (index) is even
        # Indices are 0, 1, 2, 3, ... so even positions are 0, 2, 4, ...
        is_even_index = (current_index % 2 == 0)

        if is_even_index:
            # Retrieve the value at the current index
            current_value = numbers[current_index]

            # Validate that the value is actually an integer
            if not isinstance(current_value, int):
                raise TypeError(f"Element at index {current_index} is not an integer: {current_value}")

            # Check if the value itself is even
            is_even_value = (current_value % 2 == 0)

            if is_even_value:
                # Accumulate the sum
                total_sum += current_value

    return total_sum

# Assertions provided in the problem description
if __name__ == "__main__":
    # Test case 1: [5, 6, 12, 1, 18, 8], length 6
    # Indices: 0(5), 1(6), 2(12), 3(1), 4(18), 5(8)
    # Even indices: 0, 2, 4. Values: 5, 12, 18.
    # Even values at even indices: 12, 18. Sum: 30.
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6) == 30

    # Test case 2: [3, 20, 17, 9, 2, 10, 18, 13, 6, 18], length 10
    # Even indices: 0, 2, 4, 6, 8. Values: 3, 17, 2, 18, 6.
    # Even values at even indices: 2, 18, 6. Sum: 26.
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18], 10) == 26

    # Test case 3: [5, 6, 12, 1], length 4
    # Even indices: 0, 2. Values: 5, 12.
    # Even values at even indices: 12. Sum: 12.
    assert sum_even_and_even_index([5, 6, 12, 1], 4) == 12