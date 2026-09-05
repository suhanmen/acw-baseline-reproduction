def check_Equality(s=None):
    if s is None:
        return "Not Equal"

    if not isinstance(s, str):
        return "Not Equal"

    if len(s) == 0:
        return "Not Equal"

    if len(s) == 1:
        return "Equal"

    first_char = s[0]
    last_char = s[-1]

    if first_char == last_char:
        return "Equal"
    else:
        return "Not Equal"