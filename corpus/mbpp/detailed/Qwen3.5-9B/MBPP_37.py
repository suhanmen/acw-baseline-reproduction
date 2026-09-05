# type: ignore
from typing import Any, List, Union

def validate_input(input_list: List[Any]) -> None:
    """
    Validates that the input is a list and contains only integers or strings.

    :param input_list: The list to validate.
    :raises TypeError: If the input is not a list.
    :raises ValueError: If the input contains elements that are not integers or strings.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    for index, item in enumerate(input_list):
        if not isinstance(item, (int, str)):
            raise ValueError(
                f"Element at index {index} is of unsupported type {type(item).__name__}."
            )


def separate_by_type(items: List[Any]) -> tuple:
    """
    Separates the input list into two distinct lists: one for integers and one for strings.

    :param items: The original list of mixed items.
    :return: A tuple containing (list_of_integers, list_of_strings).
    """
    integers_list: List[int] = []
    strings_list: List[str] = []

    for item in items:
        if isinstance(item, int):
            integers_list.append(item)
        elif isinstance(item, str):
            strings_list.append(item)
        # Since validation ensures no other types exist, we can ignore this elif in production
        # but keeping it for logical completeness based on type checks.

    return integers_list, strings_list


def sort_integers(numbers: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order.

    :param numbers: A list of integers.
    :return: A new list of sorted integers.
    """
    return sorted(numbers)


def sort_strings(texts: List[str]) -> List[str]:
    """
    Sorts a list of strings in ascending lexicographical order.

    :param texts: A list of strings.
    :return: A new list of sorted strings.
    """
    return sorted(texts)


def merge_sorted_lists(sorted_ints: List[int], sorted_strs: List[str]) -> List[Any]:
    """
    Merges a list of sorted integers and a list of sorted strings into a single list.
    Integers come before strings in the final output.

    :param sorted_ints: The sorted list of integers.
    :param sorted_strs: The sorted list of strings.
    :return: A combined list [integers..., strings...].
    """
    result_list: List[Any] = []

    # Extend result with integers
    result_list.extend(sorted_ints)

    # Extend result with strings
    result_list.extend(sorted_strs)

    return result_list


def sort_mixed_list(input_data: List[Any]) -> List[Any]:
    """
    Sorts a given mixed list of integers and strings.

    Logic:
    1. Validates the input is a list of integers and/or strings.
    2. Separates the list into integers and strings.
    3. Sorts the integers numerically.
    4. Sorts the strings lexicographically.
    5. Concatenates the sorted integers followed by the sorted strings.

    :param input_data: The list to be sorted.
    :return: A new list containing sorted integers followed by sorted strings.
    :raises TypeError: If input is not a list.
    :raises ValueError: If input contains non-integer/non-string elements.
    """

    # Step 1: Validation
    validate_input(input_data)

    # Handle edge case: Empty list
    if not input_data:
        return []

    # Step 2: Separate
    int_part, str_part = separate_by_type(input_data)

    # Step 3: Sort integers
    sorted_integers = sort_integers(int_part)

    # Step 4: Sort strings
    sorted_strings = sort_strings(str_part)

    # Step 5: Merge
    final_sorted_list = merge_sorted_lists(sorted_integers, sorted_strings)

    return final_sorted_list