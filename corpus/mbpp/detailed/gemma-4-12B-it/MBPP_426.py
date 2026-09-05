from typing import List, Any

def filter_oddnumbers(numbers: List[int]) -> List[int]:
    """
    Filters a list of integers and returns only the odd numbers 
    using a lambda function.

    Args:
        numbers (List[int]): A list of integers to filter.

    Returns:
        List[int]: A list containing only the odd integers from the input.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list immediately
    if len(numbers) == 0:
        return []

    # Validate that all elements in the list are integers
    for item in numbers:
        if not isinstance(item, int):
            raise ValueError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Define the logic for identifying an odd number using a lambda function.
    # An integer is odd if the remainder when divided by 2 is not zero.
    is_odd_lambda = lambda x: x % 2 != 0

    # Use the built-in filter function with the lambda.
    # filter() returns an iterator, so we cast it back to a list.
    odd_numbers_iterator = filter(is_odd_lambda, numbers)
    result_list = list(odd_numbers_iterator)

    return result_list

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert filter_oddnumbers([10, 20, 45, 67, 84, 93]) == [45, 67, 93]
    assert filter_oddnumbers([5, 7, 9, 8, 6, 4, 3]) == [5, 7, 9, 3]

    # Additional defensive test cases
    assert filter_oddnumbers([]) == []
    assert filter_oddnumbers([2, 4, 6]) == []
    assert filter_oddnumbers([1, 3, 5]) == [1, 3, 5]
    assert filter_oddnumbers([-1, -2, -3, 0]) == [-1, -3]