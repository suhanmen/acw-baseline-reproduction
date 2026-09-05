def snake_to_camel(snake_str):
    # Split the snake string into parts based on underscores
    parts = snake_str.split('_')
    # Capitalize the first letter of each part except the first
    camel = ''.join([parts[0]] + [part.capitalize() for part in parts[1:]])
    return camel