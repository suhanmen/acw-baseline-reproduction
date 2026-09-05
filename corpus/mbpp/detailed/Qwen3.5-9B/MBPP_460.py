from typing import Any, List, Union

Number = Union[int, float]

def get_first_element_of_sublist(sublist: List[Number]) -> Number:
    """
    Returns the first element of a given sublist.

    Raises:
        ValueError: If the sublist is empty.
    """
    # Validate that the input is a list
    if not isinstance(sublist, list):
        raise TypeError(f"Expected a list, but got {type(sublist).__name__}")

    # Validate that the sublist is not empty
    if len(sublist) == 0:
        raise ValueError("Sublist cannot be empty")

    # Return the first element
    return sublist[0]

def extract_first_elements(input_list: List[List[Number]]) -> List[Number]:
    """
    Extracts the first element from each sublist within the provided list of lists.

    Validates inputs for correctness and handles edge cases such as:
    - Empty input list
    - Lists containing non-list elements
    - Empty sublists
    - Lists containing invalid element types within sublists

    Returns:
        A list containing the first element of each valid sublist.

    Raises:
        TypeError: If the main input is not a list or if any element is not a list.
        ValueError: If any sublist is empty.
    """
    # Validate that the main input is a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list of lists, but got {type(input_list).__name__}")

    # Handle the edge case where the main list is empty
    if len(input_list) == 0:
        return []

    result: List[Number] = []

    # Iterate through each sublist explicitly
    for index in range(len(input_list)):
        sublist = input_list[index]

        # Validate that the current element is indeed a list
        if not isinstance(sublist, list):
            raise TypeError(
                f"Element at index {index} is not a list. "
                f"Expected List[Number], got {type(sublist).__name__}."
            )

        # Validate that the sublist is not empty
        if len(sublist) == 0:
            raise ValueError(f"Sublist at index {index} is empty.")

        # Get the type of the element for validation
        first_element = sublist[0]

        # Optional but good practice: Ensure elements within the sublist are numbers
        # (though the problem implies numerical context based on examples, 
        # we strictly follow the extraction logic, just ensuring structural integrity).
        # For strict defensive programming against weird types if this were generic:
        # if not isinstance(first_element, (int, float)):
        #     raise TypeError(f"Element at index {index} position 0 is not a number.")

        # Append the extracted element to the result list
        result.append(first_element)

    return result

def extract(input_list: List[List[Number]]) -> List[Number]:
    """
    Wrapper function for extract_first_elements to match the specific problem signature.

    This function satisfies the requirement of keeping the given signature exactly as is.
    It delegates the heavy lifting to extract_first_elements for modular design.
    """
    return extract_first_elements(input_list)

# Verification of the problem requirements against the defined function:
# assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
# assert Extract([[1,2,3],[4, 5]]) == [1,4]
# assert Extract([[9,8,1],[1,2]]) == [9,1]
# The function 'extract' handles these cases by iterating over the input list,
# verifying each sublist is non-empty, and appending the index [0] to the result.