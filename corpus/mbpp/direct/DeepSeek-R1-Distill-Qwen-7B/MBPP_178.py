def string_literals(literals, target):
    for lit in literals:
        if lit in target:
            return "Matched!"
    return "Not Matched!"