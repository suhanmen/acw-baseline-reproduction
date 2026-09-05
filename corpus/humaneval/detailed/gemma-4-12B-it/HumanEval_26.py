from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Defensive programming: Validate that the input is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected input type 'list', but received '{type(numbers).__name__}'")

    # Handle the edge case of an empty list immediately
    if not numbers:
        return []

    # Validate that all elements in the list are integers
    # This ensures the function adheres strictly to the type hint and problem description
    for index, item in enumerate(numbers):
        if not isinstance(item, int):
            raise ValueError(f"Element at index {index} is not an integer: {item}")

    # Step 1: Count the frequency of every number in the input list.
    # We use a dictionary for O(n) time complexity.
    frequency_map = {}
    for num in numbers:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    # Step 2: Construct a result list containing only elements with a frequency of 1.
    # We iterate through the original list to maintain the input order.
    result = []
    for num in numbers:
        count = frequency_map.get(num)

        # We only include the element if it appeared exactly once in the original input
        if count == 1:
            result.append(num)

    return result