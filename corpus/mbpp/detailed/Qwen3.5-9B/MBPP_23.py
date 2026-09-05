from typing import List, Union

Number = Union[int, float]
NestedList = List[Number]
NestedListOfLists = List[NestedList]


def validate_nested_list(input_list: List) -> NestedListOfLists:
    """
    Validates that the input is a list of lists containing numbers.
    Raises a TypeError if the structure is invalid.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    if len(input_list) == 0:
        raise ValueError("Input list cannot be empty.")

    for i, inner_list in enumerate(input_list):
        if not isinstance(inner_list, list):
            raise TypeError(f"Element at index {i} is not a list.")

        if len(inner_list) == 0:
            raise ValueError(f"List at index {i} is empty.")

        for j, element in enumerate(inner_list):
            if not isinstance(element, (int, float)):
                raise TypeError(f"Element at index [{i}][{j}] is not a number.")

    return input_list


def calculate_sum(sublist: NestedList) -> Number:
    """
    Calculates the sum of a single sublist.
    Uses a loop for explicit control flow as per requirements.
    """
    total_sum = 0.0
    for value in sublist:
        total_sum += value
    return total_sum


def find_maximum_sum(nested_list: NestedListOfLists) -> Number:
    """
    Finds the maximum sum of elements among all sublists in the provided nested list.

    Steps:
    1. Validate the input structure.
    2. Initialize a variable to store the maximum sum found so far.
    3. Iterate through each sublist.
    4. Calculate the sum of the current sublist.
    5. Compare with the current maximum and update if the current sum is larger.
    6. Return the final maximum sum.
    """
    # Step 1: Validate the input
    validated_input = validate_nested_list(nested_list)

    # Step 2: Initialize the maximum sum tracker
    # We initialize with a very small number or the sum of the first element
    # Since we validated non-empty lists, we can safely take the sum of the first sublist
    # as our initial maximum.

    first_sublist = validated_input[0]
    current_max_sum = calculate_sum(first_sublist)

    # Step 3 & 4: Iterate through the rest of the sublists (skip index 0 as it's already processed)
    for index in range(1, len(validated_input)):
        sublist = validated_input[index]

        # Step 4: Calculate the sum of the current sublist
        current_sublist_sum = calculate_sum(sublist)

        # Step 5: Update the maximum if the current sublist sum is greater
        if current_sublist_sum > current_max_sum:
            current_max_sum = current_sublist_sum

    return current_max_sum


# Example usage for manual verification (not included in the final assertion block):
# if __name__ == "__main__":
#     print(maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]])) # Expected: 33
#     print(maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]))             # Expected: 6
#     print(maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]])) # Expected: 19