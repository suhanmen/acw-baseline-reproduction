from typing import List, Tuple, Dict, Optional

def max_aggregate(data: List[Tuple[str, int]]) -> Optional[Tuple[str, int]]:
    """
    Calculates the maximum aggregate score from a list of (name, score) tuples.
    Aggregates scores by name and returns the name and total score of the person
    with the highest total.

    Args:
        data: A list of tuples where each tuple contains a string (name) 
              and an integer (score).

    Returns:
        A tuple containing the name and the maximum aggregate score,
        or None if the input list is empty.

    Raises:
        TypeError: If the input is not a list or contains invalid types.
        ValueError: If any tuple in the list is malformed.
    """
    # 1. Input Validation: Ensure the input is a list.
    if not isinstance(data, list):
        raise TypeError("Input must be a list of tuples.")

    # 2. Edge Case: Handle empty input.
    if len(data) == 0:
        return None

    # 3. Data Processing: Aggregate scores by name.
    # Using a dictionary to map each unique name to its running total score.
    score_map: Dict[str, int] = {}

    for item in data:
        # Validate that each element is a tuple of exactly two items.
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError(f"Invalid data format encountered: {item}. "
                             "Expected a tuple of (name, score).")

        name, score = item

        # Validate types within the tuple.
        if not isinstance(name, str):
            raise TypeError(f"Name must be a string, found {type(name)}: {name}")
        if not isinstance(score, int):
            raise TypeError(f"Score must be an integer, found {type(score)}: {score}")

        # Update the aggregate score for the name.
        if name in score_map:
            score_map[name] += score
        else:
            score_map[name] = score

    # 4. Find the maximum aggregate.
    # We need to iterate through the dictionary to find the key with the highest value.
    max_name: Optional[str] = None
    max_score: int = float('-inf')

    # Iterate through the aggregated results.
    for name, total_score in score_map.items():
        # Check if the current total score is greater than the recorded maximum.
        if total_score > max_score:
            max_score = total_score
            max_name = name
        # Handle the case where scores might be equal; 
        # current logic preserves the first one encountered in the dict iteration.
        elif total_score == max_score:
            # Explicitly keeping the first one found is standard, 
            # but we could add logic here to handle ties (e.g., alphabetical).
            pass

    # 5. Return the final result.
    if max_name is None:
        return None

    return (max_name, max_score)

if __name__ == "__main__":
    # These assertions verify the logic against the problem requirements.
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)