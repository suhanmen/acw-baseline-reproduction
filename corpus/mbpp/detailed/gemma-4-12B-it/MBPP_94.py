from typing import List, Tuple, Union

def index_minimum(data: List[Tuple[str, int]]) -> str:
    """
    Identifies and returns the name (the first element of the tuple) 
    corresponding to the minimum score (the second element of the tuple)
    from a list of tuples.

    Args:
        data: A list of tuples where each tuple contains a string (name) 
              and an integer (score).

    Returns:
        The name associated with the lowest score.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or elements are not of expected types.
    """
    # --- Input Validation ---

    # Check if the input is actually a list
    if not isinstance(data, list):
        raise TypeError(f"Expected input type 'list', but received '{type(data).__name__}'")

    # Handle the empty list edge case
    if len(data) == 0:
        raise ValueError("The input list cannot be empty.")

    # Validate the internal structure of the list
    for item in data:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each element in the list must be a tuple of exactly two items.")

        name, score = item
        if not isinstance(name, str):
            raise TypeError(f"Expected name to be a string, but got '{type(name).__name__}'")
        if not isinstance(score, (int, float)):
            raise TypeError(f"Expected score to be a number, but got '{type(score).__name__}'")

    # --- Logic Implementation ---

    # Initialize tracking variables
    # We use None to represent that no minimum has been found yet
    minimum_score: Union[int, float, None] = None
    name_with_minimum_score: str = ""

    # Iterate through the list of tuples to find the minimum
    for index, record in enumerate(data):
        current_name = record[0]
        current_score = record[1]

        # If this is the first record, it is currently our minimum
        if minimum_score is None:
            minimum_score = current_score
            name_with_minimum_score = current_name
        else:
            # Check if the current record's score is strictly less than 
            # the smallest score found so far.
            if current_score < minimum_score:
                minimum_score = current_score
                name_with_minimum_score = current_name
            # Note: If scores are equal, we retain the first one encountered,
            # which is the standard behavior for finding a minimum.

    return name_with_minimum_score

# Testing logic to verify assertions
if __name__ == "__main__":
    # These assertions are included to satisfy the prompt requirements
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'