from typing import List, Optional


def f(n: int) -> Optional[List[int]]:
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # Validate the input parameter n
    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__} instead.")

    if n < 0:
        raise ValueError(f"Parameter 'n' must be a non-negative integer, got {n} instead.")

    # Initialize the result list container
    result_list: List[int] = []

    # Track the current counter 'i' which starts from 1 as per requirements
    current_index: int = 1

    # Helper function to calculate factorial of a given number
    def calculate_factorial(number: int) -> int:
        """Calculates the factorial of a non-negative integer.

        Args:
            number: A non-negative integer.

        Returns:
            The factorial of the number.

        Raises:
            ValueError: If the number is negative.
        """
        if number < 0:
            raise ValueError(f"Factorial is not defined for negative numbers: {number}")

        factorial_result: int = 1
        counter: int = 1

        while counter <= number:
            factorial_result = factorial_result * counter
            counter = counter + 1

        return factorial_result

    # Helper function to calculate the sum of numbers from 1 to a given number
    def calculate_sum_to(number: int) -> int:
        """Calculates the sum of numbers from 1 to the given number.

        Args:
            number: A non-negative integer.

        Returns:
            The sum of integers from 1 to number.

        Raises:
            ValueError: If the number is negative.
        """
        if number < 0:
            raise ValueError(f"Sum range cannot include negative start values for this logic: {number}")

        total_sum: int = 0
        counter: int = 1

        while counter <= number:
            total_sum = total_sum + counter
            counter = counter + 1

        return total_sum

    # Generate the list elements based on the conditions
    while current_index <= n:
        # Determine which value to compute based on whether the index is even or odd
        # Note: The problem states "if i is even". In the example f(5) == [1, 2, 6, 24, 15]:
        # Index 1 (odd): 1 (sum 1..1)
        # Index 2 (even): 2 (factorial 2)
        # Index 3 (odd): 6 (sum 1..3 = 6)
        # Index 4 (even): 24 (factorial 4)
        # Index 5 (odd): 15 (sum 1..5 = 15)
        # This matches the logic: even index -> factorial, odd index -> sum.

        computed_value: int = 0

        if current_index % 2 == 0:
            # Condition: i is even
            # Compute factorial of current_index
            computed_value = calculate_factorial(current_index)
        else:
            # Condition: i is odd (otherwise)
            # Compute sum of numbers from 1 to current_index
            computed_value = calculate_sum_to(current_index)

        # Append the computed value to the result list
        result_list.append(computed_value)

        # Increment the counter for the next iteration
        current_index = current_index + 1

    return result_list