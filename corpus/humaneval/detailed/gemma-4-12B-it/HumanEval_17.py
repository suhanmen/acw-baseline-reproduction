from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    if not isinstance(music_string, str):
        raise TypeError("Input must be a string.")

    # Strip leading and trailing whitespace to ensure clean processing
    cleaned_input = music_string.strip()

    # Handle the case of an empty input string immediately
    if not cleaned_input:
        return []

    # Split the string into tokens based on whitespace.
    # This handles multiple spaces between notes correctly.
    tokens = cleaned_input.split()

    beats_list = []

    for token in tokens:
        # Determine the beat value based on the token content.
        # We use explicit conditional logic to ensure clarity and 
        # easy identification of invalid tokens.

        beat_value = None

        if token == 'o':
            # 'o' is a whole note, worth 4 beats
            beat_value = 4
        elif token == 'o|':
            # 'o|' is a half note, worth 2 beats
            beat_value = 2
        elif token == '.|':
            # '.|' is a quarter note, worth 1 beat
            beat_value = 1
        else:
            # If a token does not match any of the defined notes,
            # we raise a ValueError to maintain production-grade 
            # robustness and prevent silent failures.
            raise ValueError(f"Invalid musical note detected: '{token}'")

        # Append the validated beat value to our result list
        beats_list.append(beat_value)

    return beats_list