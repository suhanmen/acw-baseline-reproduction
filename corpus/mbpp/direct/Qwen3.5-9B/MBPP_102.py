def snake_to_camel(s):
    parts = s.split('_')
    result = parts[0].capitalize()
    for part in parts[1:]:
        result += part.capitalize()
    return result