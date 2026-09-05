def remove_splchar(s: str) -> str:
    """
    Removes all characters from the input string that are not alphanumeric.
    """
    return "".join(char for char in s if char.isalnum())

if __name__ == "__main__":
    assert remove_splchar('python  @#&^%$*program123') == 'pythonprogram123'
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language') == 'pythonprogramming24language'
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program') == 'python67program'