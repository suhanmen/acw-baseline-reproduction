from typing import List, Union

Number = Union[int, float]

def sum_negativenum(numbers: List[Number]) -> Union[int, float]:
    """
    Calculates the sum of all negative numbers in the provided list.

    This function uses a lambda expression to filter out negative numbers
    and sums them up. It includes comprehensive validation and handles edge cases.

    Args:
        numbers: A list of numeric values (integers or floats).

    Returns:
        The sum of all negative numbers in the list. Returns 0 if there are no
        negative numbers or if the input list is empty.

    Raises:
        TypeError: If the input is not a list or if any element is not a number.
        ValueError: If the input list is None.
    """

    # Step 1: Validate that the input is not None
    if numbers is None:
        raise ValueError("Input list cannot be None.")

    # Step 2: Validate that the input is actually a list
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, but received {type(numbers).__name__}.")

    # Step 3: Validate that every element in the list is a number (int or float)
    for index, item in enumerate(numbers):
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"Element at index {index} is not a number. "
                f"Expected int or float, got {type(item).__name__}."
            )

    # Step 4: Initialize a variable to hold the running sum of negative numbers
    negative_sum = 0.0

    # Step 5: Create the lambda function that checks if a number is negative
    # This lambda returns True if the number is less than zero, False otherwise.
    is_negative_check = lambda num: num < 0

    # Step 6: Iterate through each number in the list
    # We use an explicit for-loop instead of list comprehensions for clarity
    # as per the requirement to spell out steps.
    for current_number in numbers:

        # Step 7: Apply the lambda function to check if the current number is negative
        if is_negative_check(current_number):

            # Step 8: If it is negative, add it to our running sum
            negative_sum += current_number

    # Step 9: Return the calculated sum.
    # Note: The sum is initially a float due to the initialization.
    # In a strict type system, we might cast this back to int if we know all inputs are ints
    # and the result is whole, but keeping it as the native sum result is safer for floats.
    return negative_sum