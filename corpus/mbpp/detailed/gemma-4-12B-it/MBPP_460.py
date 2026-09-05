from typing import List, Any, Union

def Extract(data: List[List[Any]]) -> List[Any]:
    """
    Takes a list of lists and returns a new list containing the first 
    element of each sublist.

    Args:
        data (List[List[Any]]): A list where each element is expected to be 
                                 a list of items.

    Returns:
        List[Any]: A list of the first elements from each sublist.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element within the main list is not a list or is empty.
    """
    # 1. Validate that the input is actually a list.
    if not isinstance(data, list):
        raise TypeError(f"Input must be a list, but received {type(data).__name__}")

    # 2. Handle the edge case where the input list is empty.
    if len(data) == 0:
        return []

    # 3. Initialize the result container.
    first_elements_result = []

    # 4. Iterate through each item in the outer list.
    for index, sublist in enumerate(data):
        # Validate that the inner element is a list.
        if not isinstance(sublist, list):
            raise ValueError(
                f"Element at index {index} is not a list. Expected List[Any], "
                f"got {type(sublist).__name__}."
            )

        # Check if the sublist is empty. 
        # Since we need to "Extract" the first element, an empty list is an invalid case.
        if len(sublist) == 0:
            raise ValueError(
                f"Sublist at index {index} is empty. Cannot extract the first element."
            )

        # 5. Explicitly extract the first element.
        first_element = sublist[0]

        # 6. Append the extracted element to our result list.
        first_elements_result.append(first_element)

    # 7. Return the final compiled list.
    return first_elements_result

# Verification against provided assertions
if __name__ == "__main__":
    # These are the requirements specified in the prompt
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert Extract([[1, 2, 3], [4, 5]]) == [1, 4]
    assert Extract([[9, 8, 1], [1, 2]]) == [9, 1]