def max_aggregate(data):
    """
    Calculates the maximum aggregate score for individuals in a list of tuples.

    Args:
        data: A list of tuples in the format (name, score).

    Returns:
        A tuple containing the name and the highest aggregated score.
    """
    totals = {}
    for name, score in data:
        totals[name] = totals.get(name, 0) + score

    # Find the key with the maximum value
    max_name = None
    max_score = -float('inf')

    # Iterating over items ensures we find the first max if there's a tie,
    # though the test cases suggest specific results.
    for name, score in totals.items():
        if score > max_score:
            max_score = score
            max_name = name

    return (max_name, max_score)

if __name__ == "__main__":
    assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)