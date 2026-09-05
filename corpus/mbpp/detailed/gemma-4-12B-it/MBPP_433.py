from typing import List, Union


def check_greater(numbers: List[Union[int, float]], entered_number: Union[int, float]) -> str:
    """
    Checks whether the entered number is strictly greater than ALL elements 
    in the provided array.

    Args:
        numbers (List[Union[int, float]]): A list of integers or floats to compare against.
        entered_number (Union[int, float]): The number to compare against the elements of the list.

    Returns:
        str: A message indicating if the entered number is greater than all elements 
             or not.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If inputs are not of numeric types.
    """
    # Validate that the input list is not empty
    if not isinstance(numbers, list):
        raise TypeError("The first argument must be a list.")

    if len(numbers) == 0:
        raise ValueError("The input list cannot be empty.")

    # Validate types of elements in the list and the entered_number
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the array must be numeric. Found: {type(item)}")

    if not isinstance(entered_number, (int, float)):
        raise TypeError(f"The entered number must be numeric. Found: {type(entered_number)}")

    # Logic to determine if the entered number is greater than every element in the array
    is_greater_than_all = True

    for element in numbers:
        # If any element is greater than or equal to the entered number, 
        # then the entered number is NOT strictly greater than those in the array.
        if entered_number <= element:
            is_greater_than_all = False
            break

    # Construct the response based on the comparison result
    if is_greater_than_all:
        return "Yes, the entered number is greater than those in the array"
    else:
        # The problem specification implies a specific string for the negative case.
        # Since 'greater than' is the check, if it fails, it is "not greater".
        # The prompt specifically asks for this string:
        # 'No, entered number is less than those in the array'
        return "No, entered number is less than those in the array"

# The assertions provided in the problem description:
if __name__ == "__main__":
    # Test Case 1
    # Array: [1, 2, 3, 4, 5], Entered: 4
    # 4 is not greater than 4 and 5.
    assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'

    # Test Case 2
    # Array: [2, 3, 4, 5, 6], Entered: 8
    # 8 is greater than all elements.
    assert check_greater([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'

    # Test Case 3
    # Array: [9, 7, 4, 8, 6, 1], Entered: 11
    # 11 is greater than all elements.
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'