from typing import List, Union

def sort_mixed_list(input_list: List[Union[int, str]]) -> List[Union[int, str]]:
    """
    Sorts a mixed list of integers and strings.
    Integers are sorted numerically in ascending order.
    Strings are sorted lexicographically in ascending order.
    Integers always precede strings in the final sorted list.

    Args:
        input_list (List[Union[int, str]]): A list containing integers and strings.

    Returns:
        List[Union[int, str]]: The sorted list.

    Raises:
        TypeError: If an element in the list is neither an int nor a str.
    """
    # Handle edge case: Empty list
    if not input_list:
        return []

    # Validate input types and separate the data
    integers: List[int] = []
    strings: List[str] = []

    for item in input_list:
        # Explicit type checking for production-grade robustness
        if isinstance(item, int) and not isinstance(item, bool):
            # Note: bool is a subclass of int in Python, so we check specifically
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        else:
            raise TypeError(f"Unsupported type found in list: {type(item).__name__} (value: {item})")

    # Sort the integers numerically
    # We use a copy or the list itself since we are rebuilding the result
    sorted_integers = sorted(integers)

    # Sort the strings lexicographically
    sorted_strings = sorted(strings)

    # Combine the results: integers first, then strings
    # This ensures the behavior matches the requirement:
    # [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    result = sorted_integers + sorted_strings

    return result

if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt
    test_input = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
    expected_output = [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

    assert sort_mixed_list(test_input) == expected_output
    assert sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]) == expected_output
    assert sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]) == expected_output