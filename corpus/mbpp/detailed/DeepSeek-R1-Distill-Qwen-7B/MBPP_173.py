def remove_splchar(s: str) -> str:
    # Initialize an empty string to accumulate alphanumeric characters
    result = ""

    # Iterate through each character in the input string
    for char in s:
        # Check if the current character is alphanumeric
        if char.isalnum():
            # Append the alphanumeric character to the result string
            result += char

    # Return the cleaned string
    return result

# Test cases to verify the correctness of the function
def test_remove_splchar():
    assert remove_splchar('python  @#&^%$*program123') == ('pythonprogram123')
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language') == ('pythonprogramming24language')
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program') == ('python67program')

# Run the test cases
test_remove_splchar()