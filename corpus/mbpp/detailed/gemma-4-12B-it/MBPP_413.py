from typing import List, Tuple, Any, Union

def extract_nth_element(data: List[Tuple[Any, ...]], n: int) -> List[Any]:
    """
    Extracts the nth element from a list of tuples and returns a list 
    containing those nth elements from each tuple.

    Args:
        data: A list of tuples.
        n: The zero-based index of the element to extract from each tuple.

    Returns:
        A list of elements located at index n in each tuple.

    Raises:
        ValueError: If the input data is empty or n is out of bounds.
        TypeError: If the input data is not a list or contains non-tuple items.
    """
    # Validate that the input 'data' is indeed a list
    if not isinstance(data, list):
        raise TypeError(f"Expected input 'data' to be a list, but got {type(data).__name__}.")

    # Handle the edge case of an empty input list
    if len(data) == 0:
        raise ValueError("The input list 'data' is empty.")

    # Validate that 'n' is an integer
    if not isinstance(n, int):
        raise TypeError(f"Expected index 'n' to be an integer, but got {type(n).__name__}.")

    # Check for negative index. While Python supports negative indexing, 
    # the problem context implies standard 0-based extraction.
    if n < 0:
        raise ValueError(f"Index 'n' must be non-negative. Received: {n}")

    extracted_elements: List[Any] = []

    # Iterate through every item in the provided list
    for index_in_list, item in enumerate(data):
        # Ensure each item in the list is a tuple (or at least indexable)
        if not isinstance(item, tuple):
            raise TypeError(
                f"Item at list index {index_in_list} is not a tuple: {type(item).__name__}"
            )

        # Check if the index 'n' is valid for the current tuple
        tuple_length = len(item)
        if n >= tuple_length:
            raise IndexError(
                f"Index {n} is out of bounds for the tuple at list position {index_in_list} "
                f"(tuple length is {tuple_length})."
            )

        # Extract the specific element
        target_element = item[n]

        # Append the found element to our result list
        extracted_elements.append(target_element)

    return extracted_elements

if __name__ == "__main__":
    # Test cases provided in the problem description
    dataset = [
        ('Greyson Fulton', 98, 99), 
        ('Brady Kent', 97, 96), 
        ('Wyatt Knott', 91, 94), 
        ('Beau Turnbull', 94, 98)
    ]

    # Assertion 1: Extract index 0 (Names)
    result1 = extract_nth_element(dataset, 0)
    assert result1 == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

    # Assertion 2: Extract index 2 (Third numbers)
    result2 = extract_nth_element(dataset, 2)
    assert result2 == [99, 96, 94, 98]

    # Assertion 3: Extract index 1 (Middle numbers)
    result3 = extract_nth_element(dataset, 1)
    assert result3 == [98, 97, 91, 94]