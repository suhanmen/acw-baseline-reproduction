from typing import List, Any

def filter_evennumbers(numbers: List[Any]) -> List[int]:
    """
    Filters a list of numbers and returns only the even ones.

    This function uses a lambda function internally as required by the problem statement.
    It performs input validation to ensure the input is a list containing only integers.
    It handles edge cases such as empty lists, single-element lists, and lists with all-equal elements.

    Args:
        numbers: A list of numbers (integers) to be filtered.

    Returns:
        A list containing only the even numbers from the input list, in their original order.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """

    # Step 1: Validate that the input is indeed a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Step 2: Validate that every element in the list is an integer
    # We explicitly check for 'int' to exclude booleans, as bool is a subclass of int in Python
    for index, value in enumerate(numbers):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                f"Element at index {index} is not a valid integer (found {type(value).__name__})"
            )

    # Step 3: Define the helper logic using a lambda function
    # The lambda checks if a number modulo 2 equals 0
    even_check_lambda = lambda n: n % 2 == 0

    # Step 4: Initialize a container for the results
    # Using an empty list ensures we can handle empty input gracefully
    result_list: List[int] = []

    # Step 5: Iterate through each number explicitly
    for current_number in numbers:
        # Step 5a: Apply the lambda function to the current number
        is_even_status = even_check_lambda(current_number)

        # Step 5b: Check the result of the lambda
        if is_even_status:
            # Step 5c: Append the number to our result list if it is even
            result_list.append(current_number)

    # Step 6: Return the filtered list
    return result_list