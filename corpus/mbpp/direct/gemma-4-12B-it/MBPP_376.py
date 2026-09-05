def remove_replica(input_tuple: tuple) -> tuple:
    """
    Removes tuple elements that occur more than once and replaces the duplicates 
    with a custom value 'MSP'.
    """
    seen = set()
    result = []

    # To handle duplicates correctly, we need to keep track of what we've 
    # already seen as a "first occurrence" to ensure subsequent ones 
    # are replaced.
    for item in input_tuple:
        if item in seen:
            result.append('MSP')
        else:
            result.append(item)
            seen.add(item)

    return tuple(result)