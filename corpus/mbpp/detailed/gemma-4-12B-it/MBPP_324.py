from typing import Tuple, List, Union

def sum_of_alternates(numbers: Union[Tuple[int, ...], List[int]]) -> Tuple[int, int]:
    """
    Calculates the sum of alternate chains of numbers.

    The logic follows these steps:
    1. Validates that the input is a sequence of integers.
    2. Identifies the 'even' chain (elements at indices 0, 2, 4...) and the 'odd' chain (indices 1, 3, 5...).
    3. Computes the sum of both chains.
    4. Returns a tuple of the two sums.

    Example:
    Input: (5, 6, 3, 6, 10, 34)
    Chain 1: 5 + 3 + 10 = 18 (Wait, let's re-examine the assertion)

    Re-evaluating the assertions:
    assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)

    Wait, let's look at the indices for (5, 6, 3, 6, 10, 34):
    Idx 0: 5
    Idx 1: 6
    Idx 2: 3
    Idx 3: 6
    Idx 4: 10
    Idx 5: 34

    Sum of even indices (0, 2, 4): 5 + 3 + 10 = 18
    Sum of odd indices (1, 3, 5): 6 + 6 + 34 = 46
    The assertion says (46, 18). This means the result is (Sum of Odd Indices, Sum of Even Indices).

    Let's check the second assertion:
    assert sum_of_alternates((1, 2, 3, 4, 5)) == (6, 9)
    Idx 0: 1
    Idx 1: 2
    Idx 2: 3
    Idx 3: 4
    Idx 4: 5
    Sum of even indices (0, 2, 4): 1 + 3 + 5 = 9
    Sum of odd indices (1, 3): 2 + 4 = 6
    Assertion: (6, 9). Again, (Odd Sum, Even Sum).

    Let's check the third assertion:
    assert sum_of_alternates((6, 7, 8, 9, 4, 5)) == (21, 18)
    Idx 0: 6
    Idx 1: 7
    Idx 2: 8
    Idx 3: 9
    Idx 4: 4
    Idx 5: 5
    Sum of even indices (0, 2, 4): 6 + 8 + 4 = 18
    Sum of odd indices (1, 3, 5): 7 + 9 + 5 = 21
    Assertion: (21, 18). Consistent: (Odd Sum, Even Sum).
    """

    # 1. Type Validation
    if not isinstance(numbers, (tuple, list)):
        raise TypeError("Input must be a tuple or a list of integers.")

    # 2. Handle Empty Input
    if len(numbers) == 0:
        # Based on the logic, sums of empty sets are 0
        return (0, 0)

    # 3. Ensure all elements are integers (Defensive Programming)
    for item in numbers:
        if not isinstance(item, int):
            raise ValueError("All elements in the input sequence must be integers.")

    # 4. Separate the elements into even and odd indices
    even_index_elements = []
    odd_index_elements = []

    for index, value in enumerate(numbers):
        if index % 2 == 0:
            even_index_elements.append(value)
        else:
            odd_index_elements.append(value)

    # 5. Calculate the sums
    sum_even = 0
    for val in even_index_elements:
        sum_even += val

    sum_odd = 0
    for val in odd_index_elements:
        sum_odd += val

    # 6. Return results in the specific order required by the assertions: (Odd, Even)
    return (sum_odd, sum_even)