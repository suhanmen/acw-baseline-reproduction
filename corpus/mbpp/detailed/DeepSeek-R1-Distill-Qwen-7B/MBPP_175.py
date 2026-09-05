def is_valid_parentheses(s):
    # Define the valid pairs of parentheses
    valid_pairs = {'()', '{}', '[]'}

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Iterate through each character in the string
    for char in s:
        # If the character is an opening parenthesis, push the corresponding closing parenthesis onto the stack
        if char in valid_pairs:
            stack.append(char)
        else:
            # Check if the stack is empty, meaning there's no corresponding opening parenthesis
            if not stack:
                return False
            # Pop the last opening parenthesis and check if it matches the current closing parenthesis
            last = stack.pop()
            # If the popped parenthesis does not match the current one, return False
            if (last, char) not in valid_pairs:
                return False

    # After processing all characters, the stack should be empty if all parentheses were matched correctly
    return len(stack) == 0

# Test cases
assert is_valid_parentheses("(){}[]") == True
assert is_valid_parentheses("()[{)}") == False
assert is_valid_parentheses("()") == True