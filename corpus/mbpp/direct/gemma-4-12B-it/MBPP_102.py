def snake_to_camel(snake_str: str) -> str:
    """
    Converts a snake_case string to PascalCase (UpperCamelCase).
    """
    components = snake_str.split('_')
    # Capitalize each component and join them
    # .capitalize() handles lowercase conversion for the rest of the word
    return "".join(x.capitalize() for x in components if x)

if __name__ == "__main__":
    assert snake_to_camel('python_program') == 'PythonProgram'
    assert snake_to_camel('python_language') == 'PythonLanguage'
    assert snake_to_camel('programming_language') == 'ProgrammingLanguage'