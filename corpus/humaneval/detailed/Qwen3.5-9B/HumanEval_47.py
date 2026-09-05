from typing import List, Union, NoReturn

Number = Union[int, float]

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Define a helper function to raise a specific error for invalid input
    def _raise_invalid_input_error():
        raise ValueError("Input must be a list with at least one element.")

    # Define a helper function to validate and convert list elements
    def _validate_and_convert_to_numbers(data: List) -> List[Number]:
        converted_values: List[Number] = []
        for index, item in enumerate(data):
            if item is None:
                raise TypeError(f"Element at index {index} is None and cannot be converted to a number.")
            try:
                numeric_value: Number = float(item)
                converted_values.append(numeric_value)
            except (TypeError, ValueError) as exc:
                raise TypeError(f"Element at index {index} ({repr(item)}) is not a valid number.") from exc
        return converted_values

    # Define a helper function to sort a list of numbers
    def _sort_numbers(numbers: List[Number]) -> List[Number]:
        # Using Timsort (default for sorted()) which is O(n log n) and stable
        sorted_numbers: List[Number] = sorted(numbers)
        return sorted_numbers

    # Step 1: Validate the input type
    if not isinstance(l, list):
        _raise_invalid_input_error()

    # Step 2: Validate the input length (non-empty)
    if len(l) < 1:
        _raise_invalid_input_error()

    # Step 3: Convert all elements to numbers (floats) to ensure uniform handling
    # This handles integers, floats, and other numeric types while avoiding type errors later
    numeric_list: List[Number] = _validate_and_convert_to_numbers(l)

    # Step 4: Sort the numeric list to prepare for median calculation
    sorted_numbers: List[Number] = _sort_numbers(numeric_list)

    # Step 5: Calculate the median based on the length of the list
    # We unpack the length to explicitly handle the two cases: odd and even
    n: int = len(sorted_numbers)

    # Case A: Odd number of elements
    # The median is the middle element.
    # Index calculation: (n - 1) // 2
    # Example: [1, 2, 3] (n=3) -> index 1 -> value 2
    if n % 2 != 0:
        middle_index: int = (n - 1) // 2
        median_value: Number = sorted_numbers[middle_index]
    # Case B: Even number of elements
    # The median is the average of the two middle elements.
    # Indices are (n // 2) - 1 and (n // 2)
    # Example: [1, 2, 3, 4] (n=4) -> indices 1 and 2 -> values 2 and 3 -> avg 2.5
    else:
        first_middle_index: int = (n // 2) - 1
        second_middle_index: int = n // 2

        value_left: Number = sorted_numbers[first_middle_index]
        value_right: Number = sorted_numbers[second_middle_index]

        # Calculate the average explicitly using floating point division
        median_value: float = (value_left + value_right) / 2.0

    # Return the calculated median
    return median_value