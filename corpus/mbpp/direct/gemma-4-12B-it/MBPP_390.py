def add_string(items, prefix_template):
    """
    Inserts a given string template at the beginning of all items in a list.
    The template uses {0} as a placeholder for the item's value.
    """
    return [prefix_template.format(str(item)) for item in items]