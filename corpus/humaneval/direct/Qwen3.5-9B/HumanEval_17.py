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
    beats_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    result = []
    i = 0
    n = len(music_string)

    while i < n:
        if music_string[i] == 'o':
            if i + 1 < n and music_string[i + 1] == '|':
                result.append(2)
                i += 2
            else:
                result.append(4)
                i += 1
        elif music_string[i] == '.':
            if i + 1 < n and music_string[i + 1] == '|':
                result.append(1)
                i += 2
            else:
                # Should not happen based on problem description
                i += 1
        else:
            i += 1

    return result