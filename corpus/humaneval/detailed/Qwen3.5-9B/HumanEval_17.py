from typing import List, Optional


def _parse_single_note(note_piece: str) -> Optional[int]:
    """
    Parses a single note piece (which may contain whitespace padding) and returns
    the corresponding number of beats, or None if the note is invalid.

    Valid formats according to the problem statement:
    - 'o' (whole note) -> 4 beats
    - 'o|' (half note) -> 2 beats
    - '.|' (quarter note) -> 1 beat

    This function strips leading/trailing whitespace and handles potential
    unexpected characters or malformed notes.

    Args:
        note_piece (str): A string representing a single note, potentially with whitespace.

    Returns:
        Optional[int]: The number of beats if the note is valid, None otherwise.
    """
    # Strip whitespace from both ends of the string
    cleaned_note = note_piece.strip()

    # Check against known valid patterns
    if cleaned_note == 'o':
        return 4
    elif cleaned_note == 'o|':
        return 2
    elif cleaned_note == '.|':
        return 1
    else:
        # Invalid note format
        return None


def _parse_musical_string(music_string: str) -> List[int]:
    """
    Parses the entire musical string by splitting on whitespace and processing
    each note piece individually.

    Args:
        music_string (str): The full string containing musical notes separated by spaces.

    Returns:
        List[int]: A list of integers representing the beats for each valid note.

    Raises:
        ValueError: If the input string is empty or contains invalid note patterns.
    """
    if not music_string:
        # According to problem constraints, we should handle empty input explicitly.
        # If an empty string is passed, returning an empty list is the most logical behavior,
        # unless the problem implies it should raise an error. Given typical usage, 
        # returning [] for empty input is safe and standard.
        return []

    # Split the string by whitespace to get individual note pieces
    note_pieces = music_string.split()

    beats_list: List[int] = []

    # Iterate through each note piece and parse it
    for piece in note_pieces:
        beats = _parse_single_note(piece)

        # If the note piece was invalid, raise an error to prevent silent data loss
        # or incorrect parsing. We enforce strict validation.
        if beats is None:
            raise ValueError(
                f"Invalid musical note format found: '{piece}'. "
                f"Expected 'o' (4), 'o|' (2), or '.|' (1)."
            )

        beats_list.append(beats)

    return beats_list


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many 
    beats does each not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
        music_string (str): A string containing musical notes separated by spaces.

    Returns:
        List[int]: A list of integers where each integer represents the duration in beats
                   of the corresponding note.

    Raises:
        ValueError: If the input string is empty (though handled gracefully as []) 
                    or if any note within the string has an invalid format.

    Examples:
        >>> parse_music('o o| .| o| o| .| .| .| .| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        >>> parse_music('')
        []
        >>> parse_music('o o')
        [4, 4]
        >>> parse_music('.| .| o| o')
        [1, 1, 2, 4]
    """
    # Delegate the actual parsing logic to the helper function
    return _parse_musical_string(music_string)