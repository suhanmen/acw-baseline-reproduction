def string_literals(literals, text):
    for literal in literals:
        if literal in text:
            return 'Matched!'
    return 'Not Matched!'