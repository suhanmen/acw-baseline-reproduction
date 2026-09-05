import heapq
from typing import List, Union, Tuple


def _validate_input(
    data: Union[List, None],
    n: Union[int, None]
) -> Tuple[List[int], int]:
    """
    Validates the input arguments for heap_queue_smallest.

    Checks:
    1. 'data' must not be None.
    2. 'data' must be a list.
    3. Elements in 'data' must be integers.
    4. 'n' must not be None.
    5. 'n' must be an integer.
    6. 'n' must be non-negative.
    7. 'n' must not exceed the length of 'data'.

    Returns:
        A tuple containing the validated list of integers and the validated integer 'n'.

    Raises:
        TypeError: If types are incorrect.
        ValueError: If value constraints are violated.
    """

    # Check for None data
    if data is None:
        raise ValueError("Input list 'data' cannot be None.")

    # Check if data is a list
    if not isinstance(data, list):
        raise TypeError(f"Input 'data' must be a list, got {type(data).__name__}.")

    # Check if n is None
    if n is None:
        raise ValueError("Argument 'n' cannot be None.")

    # Check if n is an integer (excluding booleans)
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"Argument 'n' must be an integer, got {type(n).__name__}.")

    # Check if n is non-negative
    if n < 0:
        raise ValueError(f"Argument 'n' must be non-negative, got {n}.")

    # Check if n exceeds the length of data
    if n > len(data):
        raise ValueError(
            f"Argument 'n' ({n}) cannot be greater than the length of the list ({len(data)})."
        )

    # Validate each element in the list is an integer
    for index, value in enumerate(data):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                f"All elements in 'data' must be integers. "
                f"Element at index {index} is {type(value).__name__} ({value})."
            )

    return list(data), n


def _build_min_heap(data: List[int]) -> None:
    """
    Converts the list of integers into a min-heap in-place.
    This satisfies the requirement to use the heap queue algorithm.
    """
    heapq.heapify(data)


def _extract_smallest_elements(
    heap: List[int], n: int
) -> List[int]:
    """
    Extracts the smallest 'n' elements from the min-heap.

    The smallest element is at the root (index 0).
    We pop 'n' times to get the result in ascending order.

    Args:
        heap: The list being used as a heap.
        n: The number of smallest elements to extract.

    Returns:
        A list of the 'n' smallest integers in ascending order.
    """
    result_list: List[int] = []

    # Repeat n times to extract the top n elements
    for _ in range(n):
        if not heap:
            # This case should theoretically not be reached if validation passed correctly
            break

        smallest_value = heapq.heappop(heap)
        result_list.append(smallest_value)

    return result_list


def heap_queue_smallest(data: Union[List, None], n: Union[int, None]) -> List[int]:
    """
    Finds the smallest 'n' integers from a given list of numbers using the
    heap queue algorithm (heapq).

    The function validates inputs strictly, handles edge cases explicitly,
    and returns the smallest integers in ascending order.

    Args:
        data: A list of integers. Can be None (though validation will raise an error).
        n: The number of smallest integers to return. Can be None (though validation will raise an error).

    Returns:
        A list of the 'n' smallest integers from the input data, sorted in ascending order.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If input values are invalid (e.g., n < 0 or n > len(data)).
    """

    # Step 1: Validate and normalize inputs
    validated_data, validated_n = _validate_input(data, n)

    # Step 2: Handle the case where we want 0 elements
    if validated_n == 0:
        return []

    # Step 3: Handle the case where the list is empty (should be caught by validation if n > 0)
    # But just in case n was 0, we returned above. If data is empty and n > 0, validation catches it.
    if len(validated_data) == 0:
        # This block is technically unreachable due to _validate_input check 'n > len(data)'
        # if n > 0. If n was 0, we returned [].
        return []

    # Step 4: Create a working copy of the data to avoid modifying the original input list
    working_heap = list(validated_data)

    # Step 5: Transform the list into a heap in O(k) time where k is the number of elements
    _build_min_heap(working_heap)

    # Step 6: Extract the smallest 'n' elements
    smallest_elements = _extract_smallest_elements(working_heap, validated_n)

    return smallest_elements