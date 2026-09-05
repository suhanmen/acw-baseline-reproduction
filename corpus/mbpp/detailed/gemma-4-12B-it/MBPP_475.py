from typing import Dict, List, Tuple, Any

def sort_counter(counter: Dict[str, int]) -> List[Tuple[str, int]]:
    """
    Sorts a dictionary of counters by their values in descending order.

    Args:
        counter (Dict[str, int]): A dictionary where keys are strings (names)
                                   and values are integers (counts).

    Returns:
        List[Tuple[str, int]]: A list of tuples sorted by the count in 
                                descending order.

    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If the dictionary contains non-integer values or non-string keys.
    """
    # 1. Validate input type
    if not isinstance(counter, dict):
        raise TypeError(f"Expected input type 'dict', but received '{type(counter).__name__}'")

    # 2. Handle edge case: empty dictionary
    if not counter:
        return []

    # 3. Validate internal dictionary contents and prepare data for sorting
    # We convert the dict into a list of tuples to ensure we have a stable structure 
    # to work with during the sorting process.
    items_to_sort: List[Tuple[str, int]] = []

    for key, value in counter.items():
        # Validate key type
        if not isinstance(key, str):
            raise ValueError(f"Dictionary keys must be strings. Found: {type(key).__name__}")

        # Validate value type (must be an integer)
        if not isinstance(value, int):
            raise ValueError(f"Dictionary values must be integers. Found: {type(value).__name__}")

        items_to_sort.append((key, value))

    # 4. Perform the sorting
    # We want to sort by the value (index 1 of the tuple) in descending order.
    # Python's sorted() is stable, which is good practice.

    # Define a helper function to extract the value for comparison
    def get_value_for_sorting(item: Tuple[str, int]) -> int:
        return item[1]

    # Use sorted() with a key function and reverse=True for descending order
    sorted_list = sorted(
        items_to_sort, 
        key=get_value_for_sorting, 
        reverse=True
    )

    return sorted_list

# Testing the assertions provided in the prompt
if __name__ == "__main__":
    # Test Case 1
    result1 = sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})
    assert result1 == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

    # Test Case 2
    result2 = sort_counter({'Math': 400, 'Physics': 300, 'Chemistry': 250})
    assert result2 == [('Math', 400), ('Physics', 300), ('Chemistry', 250)]

    # Test Case 3
    result3 = sort_counter({'Math': 900, 'Physics': 1000, 'Chemistry': 1250})
    assert result3 == [('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]