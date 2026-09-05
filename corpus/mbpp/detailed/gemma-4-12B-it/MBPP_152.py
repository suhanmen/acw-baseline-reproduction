from typing import List, Any

def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts an array using the Merge Sort algorithm.

    Merge Sort is a stable, divide-and-conquer sorting algorithm with 
    a time complexity of O(n log n) in all cases (best, average, worst).

    Args:
        arr: A list of comparable elements (e.g., integers, floats).

    Returns:
        A new list containing the elements of the input list sorted in 
        ascending order.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains incomparable elements.
    """
    # 1. Validate input type
    if not isinstance(arr, list):
        raise TypeError(f"Input must be a list, but received {type(arr).__name__}")

    # 2. Handle base cases (empty list or single element)
    # We create a copy to ensure the original list remains unmodified (immutability).
    if len(arr) <= 1:
        return list(arr)

    # 3. Divide Phase
    # Find the midpoint of the current list
    midpoint_index = len(arr) // 2

    # Split the list into left and right halves
    left_half = arr[:midpoint_index]
    right_half = arr[midpoint_index:]

    # 4. Recursive Sort Phase
    # Recursively call merge_sort on both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 5. Merge Phase
    # Combine the two sorted halves back into a single sorted list
    return _merge(sorted_left, sorted_right)

def _merge(left_list: List[Any], right_list: List[Any]) -> List[Any]:
    """
    Helper function to merge two sorted lists into a single sorted list.

    Args:
        left_list: A sorted list of elements.
        right_list: A sorted list of elements.

    Returns:
        A single merged and sorted list.
    """
    merged_result = []
    left_pointer = 0
    right_pointer = 0

    left_len = len(left_list)
    right_len = len(right_list)

    # Compare elements from both lists and append the smaller one
    while left_pointer < left_len and right_pointer < right_len:
        left_value = left_list[left_pointer]
        right_value = right_list[right_pointer]

        try:
            if left_value <= right_value:
                merged_result.append(left_value)
                left_pointer += 1
            else:
                merged_result.append(right_value)
                right_pointer += 1
        except TypeError as e:
            raise ValueError(
                f"List contains incomparable types: {type(left_value)} and {type(right_value)}"
            ) from e

    # If there are remaining elements in left_list, append them
    # (This happens if right_list was exhausted first)
    while left_pointer < left_len:
        merged_result.append(left_list[left_pointer])
        left_pointer += 1

    # If there are remaining elements in right_list, append them
    # (This happens if left_list was exhausted first)
    while right_pointer < right_len:
        merged_result.append(right_list[right_pointer])
        right_pointer += 1

    return merged_result

if __name__ == "__main__":
    # Test cases provided in the problem description
    assert merge_sort([3, 4, 2, 6, 5, 7, 1, 9]) == [1, 2, 3, 4, 5, 6, 7, 9]
    assert merge_sort([7, 25, 45, 78, 11, 33, 19]) == [7, 11, 19, 25, 33, 45, 78]
    assert merge_sort([3, 1, 4, 9, 8]) == [1, 3, 4, 8, 9]

    # Additional edge cases
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 5, 5]) == [5, 5, 5]
    assert merge_sort([-1, -5, 0, 2, -3]) == [-5, -3, -1, 0, 2]