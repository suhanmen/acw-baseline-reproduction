from typing import List, Union


def _validate_operations(operations: List[int]) -> None:
    """
    Validates the input list 'operations'.

    This function raises a ValueError if the input is invalid.
    Valid input is defined as a list where every element is an integer.

    Edge cases handled:
    - If 'operations' is not a list.
    - If any element in 'operations' is not an integer (e.g., float, str, None).

    :param operations: The list of operations to validate.
    :raises TypeError: If 'operations' is not a list.
    :raises ValueError: If any element in 'operations' is not an int.
    """
    if not isinstance(operations, list):
        raise TypeError(
            f"Expected 'operations' to be a list of integers, but got {type(operations).__name__}."
        )

    for index, operation in enumerate(operations):
        # Check if the element is strictly an instance of int.
        # Note: In Python, booleans are subclasses of int (isinstance(True, int) is True).
        # If the problem implies strict integers (excluding bool), we check against bool first.
        # However, mathematically True == 1 and False == 0, so usually they are accepted as integers.
        # Given the problem context of "deposit and withdrawal", a boolean is semantically odd
        # but technically an integer. We will allow bools to pass as integers unless stricter 
        # validation is required. If strict non-bool integers are needed, uncomment the check below:
        # if isinstance(operation, bool):
        #     raise ValueError(f"Boolean values are not accepted at index {index}.")

        if not isinstance(operation, int):
            raise ValueError(
                f"Expected integer at index {index}, but got {type(operation).__name__}. "
                f"Value was: {operation}"
            )


def _check_balance_trajectory(operations: List[int]) -> bool:
    """
    Iterates through the operations to calculate the running balance.

    Logic:
    1. Initialize balance to 0.
    2. Iterate through each operation in the list.
    3. Add the current operation to the balance.
    4. Check immediately if the balance is strictly less than 0.
    5. If yes, return True immediately.
    6. If the loop finishes without balance going below zero, return False.

    :param operations: The validated list of integer operations.
    :return: True if balance dropped below zero at any point, False otherwise.
    """
    # Explicit initialization of the starting balance
    current_balance = 0

    # Iterate explicitly without list comprehensions to maintain step visibility
    for operation in operations:
        # Apply the operation
        current_balance += operation

        # Check the condition immediately after the update
        if current_balance < 0:
            return True

    # If we have processed all operations and balance was never below zero
    return False


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.

    :param operations: A list of integers representing deposits (positive) and withdrawals (negative).
    :return: True if the account balance falls below zero at any point during the sequence, False otherwise.
    :raises TypeError: If 'operations' is not a list.
    :raises ValueError: If any element in 'operations' is not an integer.
    """
    # Step 1: Validate the input data explicitly
    _validate_operations(operations)

    # Step 2: Execute the logic to check the balance trajectory
    return _check_balance_trajectory(operations)