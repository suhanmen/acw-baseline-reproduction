from typing import List, Union

def larg_nnum(dataset: List[Union[int, float]], n: int) -> List[Union[int, float]]:
    """
    Retrieves the n largest items from a dataset, sorted in descending order.

    Args:
        dataset: A list of numbers (integers or floats).
        n: The number of largest elements to return.

    Returns:
        A list containing the n largest numbers from the dataset in descending order.

    Raises:
        ValueError: If n is negative.
        TypeError: If dataset is not a list or contains non-numeric values.
    """
    # Step 1: Validate input types
    if not isinstance(dataset, list):
        raise TypeError(f"Expected 'dataset' to be a list, but got {type(dataset).__name__}")

    if not isinstance(n, int):
        raise TypeError(f"Expected 'n' to be an integer, but got {type(n).__name__}")

    # Step 2: Validate the value of n
    if n < 0:
        raise ValueError("The value of 'n' must be a non-negative integer.")

    # Step 3: Handle the edge case where n is 0
    if n == 0:
        return []

    # Step 4: Validate that all items in the dataset are numbers
    for item in dataset:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Dataset contains a non-numeric value: {item} of type {type(item).__name__}")

    # Step 5: Handle the edge case where the dataset is empty
    if len(dataset) == 0:
        return []

    # Step 6: Handle the case where n is larger than the dataset size
    # The problem implies we return up to n items; if n > len(dataset), 
    # we return all items sorted descending.
    effective_n = n
    if n > len(dataset):
        effective_n = len(dataset)

    # Step 7: Create a copy of the dataset to avoid mutating the original input
    # This is a defensive programming best practice.
    data_copy = list(dataset)

    # Step 8: Sort the dataset in descending order
    # We use Python's Timsort (sort method), which is O(N log N) and stable.
    data_copy.sort(key=lambda x: x, reverse=True)

    # Step 9: Extract the first n elements
    result = data_copy[:effective_n]

    return result

# The following assertions verify the requirements.
if __name__ == "__main__":
    # Test Case 1: Get 2 largest
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]

    # Test Case 2: Get 5 largest
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5) == [100, 90, 80, 70, 60]

    # Test Case 3: Get 3 largest
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3) == [100, 90, 80]