def count_Squares(width: int, height: int) -> int:
    """
    Count the total number of squares in a rectangle of given width and height.

    A square of size k x k can be placed in a grid if width >= k and height >= k.
    The number of positions for a k x k square is (width - k + 1) * (height - k + 1).
    We sum this for all possible square sizes k from 1 to min(width, height).
    """
    if width <= 0 or height <= 0:
        return 0

    limit = min(width, height)
    total = 0
    for k in range(1, limit + 1):
        count_k = (width - k + 1) * (height - k + 1)
        total += count_k

    return total