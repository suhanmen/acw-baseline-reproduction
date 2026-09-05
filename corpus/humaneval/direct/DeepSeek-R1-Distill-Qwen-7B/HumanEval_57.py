def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True

    increasing = True
    decreasing = True

    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            increasing = False
        elif l[i] < l[i + 1]:
            decreasing = False

        if not increasing and not decreasing:
            return False

    return True