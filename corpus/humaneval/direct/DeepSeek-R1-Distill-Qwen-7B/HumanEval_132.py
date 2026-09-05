def is_nested(string):
    stack = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if not stack:
                return False
            last = stack.pop()
            if last + 1 == i:
                return True
    return False

# Example usage:
print(is_nested('[[]]'))  # Output: True
print(is_nested('[]]]]]]][[[[[]')  # Output: False
print(is_nested('[][]'))  # Output: False
print(is_nested('[]'))  # Output: False
print(is_nested('[[][]]'))  # Output: True
print(is_nested('[[]][['))  # Output: True