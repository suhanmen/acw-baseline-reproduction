def is_valid_parenthese(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack[-1] if stack else None
            if top != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0