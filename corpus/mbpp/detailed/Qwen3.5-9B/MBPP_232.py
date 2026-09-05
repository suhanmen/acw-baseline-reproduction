from typing import List, Any, Union

def larg_nnum(data: List[Any], n: Union[int, float]) -> List[Any]:
    """
    Returns the n largest items from the given dataset.

    The function performs the following steps:
    1. Validates that 'data' is a list.
    2. Validates that 'n' is a non-negative integer.
    3. Handles edge cases where 'n' is 0 or larger than the length of 'data'.
    4. Sorts the data in descending order.
    5. Extracts the first 'n' elements.
    6. Returns a new list containing these elements.

    Parameters:
    - data (List[Any]): The dataset from which to extract the largest items.
    - n (Union[int, float]): The number of largest items to extract.

    Returns:
    - List[Any]: A list containing the n largest items from the data.

    Raises:
    - TypeError: If 'data' is not a list or 'n' is not a valid integer.
    - ValueError: If 'n' is negative.
    """

    # Step 1: Validate that 'data' is a list
    if not isinstance(data, list):
        raise TypeError(
            f"Expected 'data' to be a list, but received: {type(data).__name__}"
        )

    # Step 2: Validate that 'n' is an integer or a float that can be converted to an integer
    # We allow float inputs that are effectively integers (e.g., 2.0) but reject others (e.g., 2.5)
    if isinstance(n, float):
        if not n.is_integer():
            raise TypeError(
                f"Expected 'n' to be an integer or a float representing an integer, "
                f"but received a float with fractional part: {n}"
            )
        n_int = int(n)
    elif isinstance(n, int):
        n_int = n
    else:
        raise TypeError(
            f"Expected 'n' to be an integer or a float, but received: {type(n).__name__}"
        )

    # Step 3: Validate that 'n' is non-negative
    if n_int < 0:
        raise ValueError(
            f"Expected 'n' to be a non-negative integer, but received: {n_int}"
        )

    # Step 4: Handle edge case where 'n' is 0
    if n_int == 0:
        return []

    # Step 5: Handle edge case where 'n' is larger than the length of 'data'
    if n_int > len(data):
        # We will return all elements in this case, as requested by "n largest"
        # implying "as many as available up to n"
        pass 
    else:
        # If n is within bounds, we proceed with sorting and slicing
        # We do nothing here, as the logic below handles it naturally,
        # but we explicitly note that we are not truncating the list length check
        # because Python's slicing handles out-of-bounds indices gracefully.
        pass

    # Step 6: Create a copy of the data to avoid mutating the original list
    # Although not strictly required by the problem statement, this is good practice
    # for production-grade code to preserve input immutability.
    data_copy = list(data)

    # Step 7: Sort the data copy in descending order
    # We use sort with reverse=True to get descending order.
    # This is O(N log N).
    data_copy.sort(reverse=True)

    # Step 8: Extract the first 'n' elements.
    # Python's slice [:n] automatically handles cases where n > len(data)
    # by returning the entire list, satisfying our edge case handling implicitly
    # and explicitly without extra conditional logic for slicing.
    result = data_copy[:n_int]

    return result