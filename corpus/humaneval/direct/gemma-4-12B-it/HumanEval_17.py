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
    # Split the string into potential symbols by whitespace
    parts = music_string.split()
    result = []

    for part in parts:
        if part == 'o':
            result.append(4)
        elif part == 'o|':
            result.append(2)
        elif part == '.|':
            result.append(1)

    return result