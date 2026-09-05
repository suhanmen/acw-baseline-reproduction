from collections import Counter
from typing import List, Union

Number = Union[int, float]

def _get_element_counts(input_list: List[Number]) -> Counter:
    """
    Helper function to count occurrences of each element in a given list.

    This function iterates over the input list and populates a Counter object.

    Args:
    input_list (List[Number]): The list of numbers to count.

    Returns:
    Counter: A dictionary-like object mapping each unique number to its count.
    """
    return Counter(input_list)

def _find_common_pairs(count_a: Counter, count_b: Counter, count_c: Counter) -> int:
    """
    Helper function to find the count of pairs that are common across three lists.

    A "pair" here refers to the combination of elements that appear together in 
    the same relative positions across the lists. However, given the problem context,
    it seems we are looking for the count of indices where all three lists have
    the same pair of values when considering elements at specific positions.

    Upon re-evaluating the problem statement and examples, it becomes clear that
    we are counting the number of pairs (value from list A, value from list B)
    that are also present as a pair in list C, considering all unique pairs 
    formed by any element from list A and any element from list B that also
    exist as a pair in list C.

    However, looking at the examples:
    count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3

    It appears that we are counting the number of indices 'i' such that:
    list_A[i] == list_B[i] and list_B[i] == list_C[i].

    Let's verify with the first example:
    List A: [1,2,3,4,5,6,7,8]
    List B: [2,2,3,1,2,6,7,9]
    List C: [2,1,3,1,2,6,7,9]

    Index 0: A[0]=1, B[0]=2, C[0]=2 -> Not equal
    Index 1: A[1]=2, B[1]=2, C[1]=1 -> Not equal
    Index 2: A[2]=3, B[2]=3, C[2]=3 -> Equal (Match)
    Index 3: A[3]=4, B[3]=1, C[3]=1 -> Not equal
    Index 4: A[4]=5, B[4]=2, C[4]=2 -> Not equal
    Index 5: A[5]=6, B[5]=6, C[5]=6 -> Equal (Match)
    Index 6: A[6]=7, B[6]=7, C[6]=7 -> Equal (Match)
    Index 7: A[7]=8, B[7]=9, C[7]=9 -> Not equal

    Total matches: 3. This matches the first assertion.

    Therefore, the function should count the number of indices where all three lists have the same value.

    However, the problem statement says "count the same pair in three given lists".
    If we interpret "pair" as the combination of two consecutive elements, let's check:

    Example 1:
    List A: [1,2,3,4,5,6,7,8] -> Pairs: (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8)
    List B: [2,2,3,1,2,6,7,9] -> Pairs: (2,2), (2,3), (3,1), (1,2), (2,6), (6,7), (7,9)
    List C: [2,1,3,1,2,6,7,9] -> Pairs: (2,1), (1,3), (3,1), (1,2), (2,6), (6,7), (7,9)

    Common pairs between all three lists:
    (2,3) is in B and C but not in A.
    (1,2) is in A and C but not in B.
    (6,7) is in all three lists.
    (7,9) is in B and C but not in A.

    Only one common pair (6,7) is found, which does not match the assertion of 3.

    Given the discrepancy, let's reconsider the problem statement. 
    The term "pair" might be a misnomer, and the actual requirement is to count 
    the number of elements that are present in all three lists at the same index.

    Let's re-examine the examples with this interpretation:

    Example 1:
    Index 2: A[2]=3, B[2]=3, C[2]=3 -> Match
    Index 5: A[5]=6, B[5]=6, C[5]=6 -> Match
    Index 6: A[6]=7, B[6]=7, C[6]=7 -> Match
    Total: 3 matches. This matches the first assertion.

    Example 2:
    List A: [1,2,3,4,5,6,7,8]
    List B: [2,2,3,1,2,6,7,8]
    List C: [2,1,3,1,2,6,7,8]

    Index 0: A[0]=1, B[0]=2, C[0]=2 -> No
    Index 1: A[1]=2, B[1]=2, C[1]=1 -> No
    Index 2: A[2]=3, B[2]=3, C[2]=3 -> Yes
    Index 3: A[3]=4, B[3]=1, C[3]=1 -> No
    Index 4: A[4]=5, B[4]=2, C[4]=2 -> No
    Index 5: A[5]=6, B[5]=6, C[5]=6 -> Yes
    Index 6: A[6]=7, B[6]=7, C[6]=7 -> Yes
    Index 7: A[7]=8, B[7]=8, C[7]=8 -> Yes
    Total: 4 matches. This matches the second assertion.

    Example 3:
    List A: [1,2,3,4,2,6,7,8]
    List B: [2,2,3,1,2,6,7,8]
    List C: [2,1,3,1,2,6,7,8]

    Index 0: A[0]=1, B[0]=2, C[0]=2 -> No
    Index 1: A[1]=2, B[1]=2, C[1]=1 -> No
    Index 2: A[2]=3, B[2]=3, C[2]=3 -> Yes
    Index 3: A[3]=4, B[3]=1, C[3]=1 -> No
    Index 4: A[4]=2, B[4]=2, C[4]=2 -> Yes
    Index 5: A[5]=6, B[5]=6, C[5]=6 -> Yes
    Index 6: A[6]=7, B[6]=7, C[6]=7 -> Yes
    Index 7: A[7]=8, B[7]=8, C[7]=8 -> Yes
    Total: 5 matches. This matches the third assertion.

    Conclusion: The function should count the number of indices where all three lists have the same value.

    Args:
    count_a (Counter): The count of elements in the first list.
    count_b (Counter): The count of elements in the second list.
    count_c (Counter): The count of elements in the third list.

    Returns:
    int: The number of indices where all three lists have the same value.
    """
    common_count = 0
    min_length_a = len(list_a)
    min_length_b = len(list_b)
    min_length_c = len(list_c)
    min_length = min_length_a if min_length_a < min_length_b else min_length_b
    min_length = min_length if min_length < min_length_c else min_length_c

    for i in range(min_length):
        if list_a[i] == list_b[i] and list_b[i] == list_c[i]:
            common_count += 1

    return common_count

def count_samepair(list_a: List[Number], list_b: List[Number], list_c: List[Number]) -> int:
    """
    Counts the number of indices where all three given lists have the same value.

    This function validates the inputs to ensure they are lists and contains only numbers.
    It then iterates through the lists up to the length of the shortest list and counts
    the number of indices where all three lists have the same value at that index.

    Args:
    list_a (List[Number]): The first list of numbers.
    list_b (List[Number]): The second list of numbers.
    list_c (List[Number]): The third list of numbers.

    Returns:
    int: The count of indices where all three lists have the same value.

    Raises:
    TypeError: If any of the inputs are not lists.
    ValueError: If any of the lists contain non-numeric elements.
    """
    # Validate input types
    if not isinstance(list_a, list):
        raise TypeError(f"Expected list_a to be a list, got {type(list_a)}")
    if not isinstance(list_b, list):
        raise TypeError(f"Expected list_b to be a list, got {type(list_b)}")
    if not isinstance(list_c, list):
        raise TypeError(f"Expected list_c to be a list, got {type(list_c)}")

    # Validate list contents for numeric types
    for idx, item in enumerate(list_a):
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise ValueError(f"Non-numeric element found in list_a at index {idx}: {item}")

    for idx, item in enumerate(list_b):
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise ValueError(f"Non-numeric element found in list_b at index {idx}: {item}")

    for idx, item in enumerate(list_c):
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise ValueError(f"Non-numeric element found in list_c at index {idx}: {item}")

    # Determine the minimum length among the three lists
    length_a = len(list_a)
    length_b = len(list_b)
    length_c = len(list_c)
    min_length = length_a if length_a < length_b else length_b
    min_length = min_length if min_length < length_c else length_c

    # Initialize counter for common elements
    common_count = 0

    # Iterate through the lists up to the minimum length
    for i in range(min_length):
        value_a = list_a[i]
        value_b = list_b[i]
        value_c = list_c[i]

        # Check if all three values are the same at the current index
        if value_a == value_b and value_b == value_c:
            common_count += 1

    return common_count