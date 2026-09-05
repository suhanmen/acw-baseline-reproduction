from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.


    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return _calculate_differences(game, guess)


def _validate_single_list(list_data: List[int], list_name: str) -> None:
    """Validate that the provided list is of type list and contains only integers."""
    if not isinstance(list_data, list):
        raise TypeError(f"{list_name} must be a list, got {type(list_data).__name__}")

    for index, item in enumerate(list_data):
        if not isinstance(item, int):
            raise TypeError(
                f"All elements in {list_name} must be integers. "
                f"Found element {item} (type: {type(item).__name__}) at index {index}"
            )


def _validate_lengths(list1: List[int], list2: List[int]) -> None:
    """Ensure that both input lists have the same length."""
    length1 = len(list1)
    length2 = len(list2)

    if length1 != length2:
        raise ValueError(
            f"Lists must be of equal length. "
            f"Received length {length1} for the first list and length {length2} for the second list."
        )


def _calculate_differences(game: List[int], guess: List[int]) -> List[int]:
    """
    Calculate the absolute difference between corresponding elements in the game and guess lists.
    If a guess matches the game score exactly, the difference is 0.
    Otherwise, it is the absolute difference.

    Since abs(x - x) is always 0, this logic simplifies to calculating the absolute difference
    for every pair, covering both correct guesses (result 0) and incorrect guesses (result > 0).
    """
    # Store validated inputs with descriptive names for the duration of processing
    game_scores: List[int] = game
    player_guesses: List[int] = guess

    # Calculate the expected output length upfront
    output_length = len(game_scores)

    # Initialize the result list with zeros
    differences: List[int] = [0] * output_length

    # Process each match index one by one
    for index in range(output_length):
        current_score = game_scores[index]
        current_guess = player_guesses[index]

        # Calculate the raw difference
        raw_difference = current_score - current_guess

        # Calculate the absolute difference
        abs_difference = abs(raw_difference)

        # Assign the result to the output list at the current index
        differences[index] = abs_difference

    # Return the computed differences
    return differences