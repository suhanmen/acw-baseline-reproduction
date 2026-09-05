from typing import List, Any, TypeVar

T = TypeVar('T')

def list_split(input_list: List[T], n: int) -> List[List[T]]:
    """
    Splits a list into multiple sublists based on the nth element.

    The logic follows a "round-robin" distribution where the first 
    sublist contains the 1st, (n+1)th, (2n+1)th... elements.
    The second sublist contains the 2nd, (n+2)th, (2n+2)th... elements,
    and so on, until the nth sublist.

    Args:
        input_list: A list of elements of any type.
        n: The interval at which to split/distribute the elements.

    Returns:
        A list of lists, where each sublist contains elements at 
        specific intervals.

    Raises:
        ValueError: If n is less than 1.
        TypeError: If input_list is not a list or n is not an integer.
    """
    # --- Input Validation ---

    if not isinstance(input_list, list):
        raise TypeError(f"Expected input_list to be of type list, got {type(input_list).__name__}")

    if not isinstance(n, int):
        raise TypeError(f"Expected n to be of type int, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"n must be a positive integer greater than 0, got {n}")

    # --- Edge Case Handling ---

    # If the input list is empty, return an empty list.
    if not input_list:
        return []

    # If n is larger than the list length, we still need to distribute 
    # elements into n buckets as per the logic, but many buckets might be empty.
    # However, looking at the test cases:
    # list_split(['a', 'b', 'c'], 3) -> [['a'], ['b'], ['c']]
    # The number of sublists produced is determined by n.

    # --- Implementation ---

    # Initialize a list of empty lists (buckets).
    # There will be exactly 'n' buckets.
    result_buckets: List[List[T]] = []
    for i in range(n):
        result_buckets.append([])

    # Iterate through the input list by index.
    # We use the modulo operator to determine which bucket an element belongs to.
    # Index 0 goes to bucket 0, Index 1 to bucket 1, ..., Index n-1 to bucket n-1.
    # Index n goes to bucket 0, etc.
    for current_index, value in enumerate(input_list):
        # Calculate the bucket index (0 to n-1).
        bucket_index = current_index % n

        # Append the value to the appropriate bucket.
        result_buckets[bucket_index].append(value)

    # --- Post-processing ---

    # According to the provided assertions:
    # list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3)
    # The result has 3 sublists. 
    # Even if a bucket ended up empty (e.g., list is shorter than n), 
    # the current logic preserves n buckets.

    # However, let's double check the assertion:
    # list_split(['python','java','C','C++','DBMS','SQL'],2)
    # Here, length is 6, n is 2. Result is 2 sublists.
    # The logic seems to produce exactly n sublists.

    # There is one nuance: If the input list is shorter than n, 
    # some buckets in result_buckets will be empty. 
    # Based on the patterns, we should return all n buckets.

    return result_buckets