from typing import List, Dict, Any, Union

def convert_list_dictionary(
    keys_list: List[Any], 
    values_list: List[Any], 
    scores_list: List[Union[int, float]]
) -> List[Dict[Any, Dict[Any, Union[int, float]]]]:
    """
    Converts three separate lists into a list of nested dictionaries.
    Each inner dictionary contains one key from keys_list, which maps 
    to another dictionary containing one value from values_list, 
    which maps to a score from scores_list.

    Args:
        keys_list: A list of identifiers (e.g., "S001").
        values_list: A list of names/items (e.g., "Adina Park").
        scores_list: A list of numerical scores (e.g., 85).

    Returns:
        A list of nested dictionaries formatted as:
        [{key1: {value1: score1}}, {key2: {value2: score2}}, ...]

    Raises:
        ValueError: If the input lists are of unequal lengths.
        TypeError: If any input is not a list.
    """

    # --- Input Validation ---

    # Ensure all inputs are actually lists
    if not isinstance(keys_list, list):
        raise TypeError("The first argument 'keys_list' must be a list.")
    if not isinstance(values_list, list):
        raise TypeError("The second argument 'values_list' must be a list.")
    if not isinstance(scores_list, list):
        raise TypeError("The third argument 'scores_list' must be a list.")

    # Check for equal lengths
    len_keys = len(keys_list)
    len_values = len(values_list)
    len_scores = len(scores_list)

    if not (len_keys == len_values == len_scores):
        raise ValueError(
            f"All input lists must have the same length. "
            f"Found lengths: keys={len_keys}, values={len_values}, scores={len_scores}"
        )

    # --- Processing ---

    # Initialize the result container
    result_list: List[Dict[Any, Dict[Any, Union[int, float]]]] = []

    # Handle the case where lists are empty
    if len_keys == 0:
        return result_list

    # Iterate through the indices of the lists
    # Using range ensures we access the same index across all three lists
    for i in range(len_keys):
        # Extract elements for the current index
        current_key = keys_list[i]
        current_value = values_list[i]
        current_score = scores_list[i]

        # Construct the inner dictionary
        # Format: {value: score}
        inner_dict = {}
        inner_dict[current_value] = current_score

        # Construct the outer dictionary
        # Format: {key: inner_dict}
        outer_dict = {}
        outer_dict[current_key] = inner_dict

        # Append the constructed dictionary to our result list
        result_list.append(outer_dict)

    return result_list

if __name__ == "__main__":
    # Verification of the logic using provided assertions
    assert convert_list_dictionary(
        ["S001", "S002", "S003", "S004"],
        ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],
        [85, 98, 89, 92]
    ) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

    assert convert_list_dictionary(
        ["abc", "def", "ghi", "jkl"],
        ["python", "program", "language", "programs"],
        [100, 200, 300, 400]
    ) == [{'abc': {'python': 100}}, {'def': {'program': 200}}, {'ghi': {'language': 300}}, {'jkl': {'programs': 400}}]

    assert convert_list_dictionary(
        ["A1", "A2", "A3", "A4"],
        ["java", "C", "C++", "DBMS"],
        [10, 20, 30, 40]
    ) == [{'A1': {'java': 10}}, {'A2': {'C': 20}}, {'A3': {'C++': 30}}, {'A4': {'DBMS': 40}}]