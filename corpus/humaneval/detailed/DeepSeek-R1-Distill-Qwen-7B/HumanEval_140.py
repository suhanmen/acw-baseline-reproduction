def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 

    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    if not text:
        return text  # handle empty input

    result = []
    current = []
    space_count = 0

    for char in text:
        if char == ' ':
            current.append(' ')
            space_count += 1
        else:
            if current and current[-1] == ' ':
                # End of a space segment
                if space_count == 1:
                    result.append('_')
                elif space_count > 2:
                    result.append('-')
                else:
                    pass  # already handled in appending
                current = []
                space_count = 0
            else:
                # End of a non-space segment, add to result
                result.append(''.join(current))
                current = [char]

    # Add the last segment if it's spaces
    if current and current[-1] == ' ':
        if space_count == 1:
            result.append('_')
        elif space_count > 2:
            result.append('-')
        else:
            pass

    # Add the last non-space segment if any
    if current:
        result.append(''.join(current))

    return ''.join(result)