from typing import List, Any

def cube_nums(numbers: List[Any]) -> List[int]:
    """
    Takes a list of numbers and returns a new list where each element 
    is the cube of the corresponding element in the input list.
    Uses a lambda function to perform the transformation.

    Args:
        numbers (List[Any]): A list of numerical values (int or float).

    Returns:
        List[int]: A list of cubed values.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    """
    # Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, but received {type(numbers).__name__}")

    # Handle the edge case of an empty list immediately
    if len(numbers) == 0:
        return []

    # Define the lambda function for cubing a single number
    # We use a lambda as requested by the problem statement.
    cube_operation = lambda x: x ** 3

    cubed_list = []

    # Iterate through the input list to process each element
    for item in numbers:
        # Validate that each item is a number (int or float)
        # This prevents the code from crashing with unhelpful errors 
        # if a string or None is passed inside the list.
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in the list must be numbers. Found: {type(item).__name__}")

        # Apply the lambda function to the current item
        cubed_value = cube_operation(item)

        # Cast to int if it's a whole number to match the expected output format 
        # (e.g., 1000 instead of 1000.0), otherwise keep as float.
        if isinstance(cubed_value, float) and cubed_value.is_integer():
            cubed_value = int(cubed_value)

        # Append the result to our result list
        cubed_list.append(cubed_value)

    return cubed_list

# Explicitly verifying the provided assertions to ensure correctness
if __name__ == "__main__":
    # Test Case 1
    result1 = cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result1 == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

    # Test Case 2
    result2 = cube_nums([10, 20, 30])
    assert result2 == [1000, 8000, 27000]

    # Test Case 3
    result3 = cube_nums([12, 15])
    assert result3 == [1728, 3375]