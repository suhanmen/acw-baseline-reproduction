def combinations_list(items):
    """
    Finds all possible combinations of the elements of a given list.
    The order of combinations and the elements within them must match 
    the specific pattern required by the assertions.
    """
    result = [[]]
    for item in items:
        # For each new item, we create new combinations by taking all 
        # existing combinations and appending the new item to them.
        new_combinations = []
        for combination in result:
            new_combinations.append(combination + [item])
        result.extend(new_combinations)

    # The expected output follows a specific nested order: 
    # For each element added, the new combinations are appended to the end.
    # However, the assertions show the new combinations are placed 
    # after the previous results in a specific sequence.
    # Let's re-evaluate the logic based on the assertion structure:
    # []
    # [item1]
    # [item2], [item2, item1]
    # [item3], [item3, item1], [item3, item2], [item3, item2, item1]

    # Let's re-implement to match the exact order in the assertions.
    final_result = [[]]
    for item in items:
        current_count = len(final_result)
        for i in range(current_count):
            # New combinations are formed by taking an existing combination 
            # and prefixing the current 'item' to it.
            # Looking at the assertion: 
            # ['orange'] comes after []
            # ['red'], ['red', 'orange'] comes after ['orange']
            # This means for every existing combo 'c', we create [item] + c.
            # But the base 'c' used are the ones that were already in the list.
            pass

    # Correct Logic to match the assertion order:
    # The list starts with [].
    # Then for 'orange', we add ['orange'].
    # Then for 'red', we add ['red'] and ['red', 'orange'].
    # Then for 'green', we add ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'].
    # The pattern is: for each new item, create a new list of combinations 
    # where the new item is at the front, followed by all combinations 
    # generated from the previous items.

    res = [[]]
    for item in items:
        new_items = []
        for existing in res:
            new_items.append([item] + existing)
        res.extend(new_items)

    return res

# The above logic actually produces:
# []
# [orange]
# [red], [red, orange]
# [green], [green, orange], [green, red], [green, red, orange]
# This matches the assertion exactly.