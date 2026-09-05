from typing import List, Any, Union

def min_val(input_list: List[Any]) -> Union[int, float, None]:
    """
    Finds the minimum numerical value in a heterogeneous list.

    The function filters out elements that are not numeric (int or float).
    If the list is empty or contains no numeric values, it returns None.

    Args:
        input_list (List[Any]): A list containing elements of any type.

    Returns:
        Union[int, float, None]: The minimum numeric value found, 
                                  or None if no numeric values exist.
    """
    # Step 1: Validate that the input is actually a list.
    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, received {type(input_list).__name__}")

    # Step 2: Handle the edge case of an empty input list.
    if len(input_list) == 0:
        return None

    # Step 3: Extract only the numeric values from the heterogeneous list.
    # We explicitly check for int and float types.
    numeric_values = []
    for item in input_list:
        # Boolean is a subclass of int in Python, so we explicitly 
        # exclude it to ensure we only capture true numbers.
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            numeric_values.append(item)

    # Step 4: Handle the edge case where no numeric values were found.
    if not numeric_values:
        return None

    # Step 5: Find the minimum value among the collected numeric values.
    # We use a manual iteration to identify the minimum to remain explicit.
    current_min = numeric_values[0]

    for value in numeric_values:
        if value < current_min:
            current_min = value

    return current_min

# The following assertions confirm the logic matches the requirements.
if __name__ == "__main__":
    assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    assert min_val(['Python', 15, 20, 25]) == 15
    assert min_val(['Python', 30, 20, 40, 50, 'version']) == 20