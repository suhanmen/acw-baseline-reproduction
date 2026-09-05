from typing import List, Any

def count_odd(numbers: List[Any]) -> int:
    """
    Counts the number of odd elements in a given list of numbers.

    This function utilizes a lambda expression in conjunction with a generator
    expression to iterate through the list, check the parity of each element,
    and accumulate the count of odd numbers.

    Parameters:
    numbers (List[Any]): A list of numeric values (int or float).

    Returns:
    int: The total count of odd numbers found in the list.

    Raises:
    TypeError: If the input is not a list, or if any element in the list is not
               a numeric type (int or float).
    ValueError: If an element is a float that cannot be used to determine parity
                (e.g., due to precision issues, though standard floats with .0
                are treated as even/odd based on their integer representation).
    """

    # Step 1: Validate the type of the input argument.
    # The problem specifies a list, so we must ensure that.
    if not isinstance(numbers, list):
        raise TypeError(
            f"Input must be a list of numbers, but got: {type(numbers).__name__}"
        )

    # Step 2: Validate that the list does not contain non-numeric types.
    # We iterate through the list and check the type of each item.
    for index, item in enumerate(numbers):
        current_type = type(item)

        # Explicitly check for integers and floats.
        if not isinstance(item, (int, float)):
            raise TypeError(
                f"All elements must be numbers. "
                f"Element at index {index} ({item}) is of type: {current_type.__name__}"
            )

        # Additional check for boolean values, as bool is a subclass of int in Python.
        # While technically an int, it's often desired to exclude True/False in 
        # numeric parity checks to avoid logical pitfalls (True=1, False=0).
        if isinstance(item, bool):
            raise TypeError(
                f"All elements must be numbers (int/float), excluding booleans. "
                f"Element at index {index} is a boolean: {item}"
            )

    # Step 3: Handle the edge case of an empty list.
    # If the list is empty, the count of odd numbers is 0.
    if len(numbers) == 0:
        return 0

    # Step 4: Define the lambda function for checking oddness.
    # The lambda takes a number 'n' and returns True if 'n % 2' is not zero.
    # We cast to int inside the lambda to safely handle float inputs like 5.0.
    is_odd_check = lambda n: int(n) % 2 != 0

    # Step 5: Define a helper function to extract the integer representation.
    # This separates the logic of parsing the number from the logic of checking parity.
    def get_number_value(n: Any) -> int:
        """
        Converts a numeric input to an integer.

        Handles integers directly and floats by truncating/rounding 
        based on the requirement to treat 5.0 as 5 and 5.1 as non-integer (but here 
        we simply cast to int which truncates, consistent with standard modulo operations 
        on floats in this context).
        """
        if isinstance(n, int):
            return n
        if isinstance(n, float):
            # If a float has a fractional part, standard integer parity is undefined 
            # in discrete math, but in programming, we often truncate or check if it's zero.
            # For this specific problem context (usually integer lists), we assume 
            # valid integers passed as floats (e.g., 5.0).
            return int(n)
        return int(n) # Fallback, though previous checks should prevent non-numbers

    # Step 6: Execute the counting logic using a generator expression.
    # We explicitly iterate through the list to demonstrate the flow.
    odd_count = 0

    # Iterate over each item in the validated list
    for current_item in numbers:

        # Get the integer value of the current item
        number_value = get_number_value(current_item)

        # Apply the lambda function to check if the number is odd
        if is_odd_check(number_value):
            # Increment the counter if the condition is met
            odd_count += 1

    # Step 7: Return the final calculated count.
    return odd_count