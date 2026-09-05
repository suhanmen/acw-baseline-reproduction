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
    # Validate input types to ensure they are lists
    if not isinstance(game, list) or not isinstance(guess, list):
        raise TypeError("Both 'game' and 'guess' must be lists of integers.")

    # Validate that the lengths of the two lists are identical
    game_length = len(game)
    guess_length = len(guess)

    if game_length != guess_length:
        raise ValueError("The 'game' and 'guess' lists must have the same length.")

    # Handle the edge case of empty lists explicitly
    if game_length == 0:
        return []

    # Initialize an empty list to store the differences
    differences: List[int] = []

    # Iterate through every pair of scores and guesses by index
    for index in range(game_length):
        score = game[index]
        prediction = guess[index]

        # Ensure the elements are actually integers
        if not isinstance(score, int) or not isinstance(prediction, int):
            raise TypeError(f"Elements at index {index} must be integers.")

        # Calculate the absolute difference
        # If score == prediction, the result is naturally 0.
        # If they differ, it returns the positive distance.
        difference_value = abs(score - prediction)

        # Append the result to our results list
        differences.append(difference_value)

    return differences