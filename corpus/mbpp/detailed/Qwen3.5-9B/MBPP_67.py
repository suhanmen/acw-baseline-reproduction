import math
from typing import Union

def _factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n.

    This is a helper function to ensure the factorial logic is isolated and clear.
    It handles the base cases explicitly.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Factorial input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Factorial is not defined for negative numbers, got {n}")

    result: int = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def bell_number(n: int) -> int:
    """
    Calculates the nth Bell number, which represents the number of ways 
    to partition a set of n elements.

    The Bell numbers can be computed using the Bell Triangle (also known as 
    Aitken's array) method, which is efficient and numerically stable for 
    integer arithmetic. Alternatively, one could use Stirling numbers of the 
    second kind summed over all partitions from 0 to n-1, but the Bell Triangle 
    is often simpler to implement with integer-only arithmetic to avoid floating 
    point errors or large intermediate fractions.

    However, for very large n (like 56 as seen in the requirements), the 
    Bell Triangle can become memory-intensive if we store the whole triangle. 
    We only need the previous row to calculate the current row.

    We will use the Bell Triangle property:
    B(n, 0) = B(n-1, n-1)
    B(n, k) = B(n, k-1) + B(n-1, k-1) for k > 0.

    The nth Bell number is B(n+1, 0) if we start with the triangle for n=0.
    Actually, let's define the sequence such that:
    Row 0: [1] -> Bell(0) = 1
    Row 1: [1, 2] -> Bell(1) = 1 (first element), Bell(2) = 2 (last element? No.)

    Let's clarify the Bell Triangle definition:
    A(n, 0) = A(n-1, n-1)
    A(n, k) = A(n, k-1) + A(n-1, k-1) for k > 0.

    Row 0: [1]  (Bell number for n=0 is 1)
    Row 1: [1, 2] (Start with last of prev (1). 1+1=2)
    Row 2: [2, 3, 5] (Start with last of prev (2). 2+1=3, 3+2=5)
    Row 3: [5, 7, 10, 15] (Start with 5. 5+2=7, 7+3=10, 10+5=15)

    Bell(n) is the first element of Row n.
    Bell(0) = 1
    Bell(1) = 1
    Bell(2) = 2
    Bell(3) = 5
    Bell(4) = 15
    Bell(5) = 52

    Let's verify the requirement: bell_number(2) == 2.
    My trace: Row 2 starts with 2. Correct.

    The algorithm:
    1. Handle n=0 explicitly if needed, though the loop handles it.
    2. Initialize the first row as [1].
    3. Iterate from i = 1 to n to generate the next rows.
    4. In each iteration, create a new row. The first element is the last element of the previous row.
    5. Subsequent elements are the sum of the current previous element and the element above-left.
    6. After computing up to row n, return the first element of that row.

    For n=56, this requires 57 rows. The max number in the last element of row 56 will be huge, 
    but Python handles arbitrary precision integers automatically.

    Args:
        n (int): A non-negative integer representing the size of the set.

    Returns:
        int: The nth Bell number.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, got {n}")

    # Edge case: Bell number of 0 is 1.
    # Our generation logic:
    # Start with row 0: [1]
    # If n=0, we return the first element of row 0, which is 1.

    # current_row will store the current row of the Bell Triangle.
    # We start with the 0-th row.
    current_row: list[int] = [1]

    # We need to generate rows until we have the n-th row.
    # current_row represents row i initially.
    # We iterate i from 1 to n to build up to the n-th row.

    for i in range(1, n + 1):
        # The first element of the new row is the last element of the previous row.
        first_element: int = current_row[-1]

        # Build the new row.
        # new_row[k] = new_row[k-1] + current_row[k-1]
        # We can do this in a loop to build the list.

        new_row: list[int] = [first_element]

        # current_row has length i (since row 0 has length 1, row 1 has length 2, ..., row i-1 has length i)
        # We need to compute i more elements for the new row of length i+1.
        # The index k goes from 1 to i (inclusive).
        # new_row[k] depends on new_row[k-1] and current_row[k-1].

        for k in range(1, i + 1):
            # k-1 is the index in the previous row.
            # k-1 is the index in the current new_row (since new_row[0] exists).
            val_from_prev_row: int = current_row[k - 1]
            val_from_current_row_start: int = new_row[k - 1]

            next_val: int = val_from_current_row_start + val_from_prev_row
            new_row.append(next_val)

        # Move to the next iteration
        current_row = new_row

    # The result is the first element of the n-th row.
    return current_row[0]